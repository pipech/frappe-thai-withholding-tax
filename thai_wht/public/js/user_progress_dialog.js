frappe.provide('frappe.setup');
frappe.provide('frappe.ui');

frappe.ui.toolbar.Toolbar.prototype.setup_progress_dialog = function() {
    frappe.call({
        method: 'frappe.desk.user_progress.get_user_progress_slides',
        callback: function(r) {
            if (r.message) {
                let slides = r.message;
                if (slides.length && slides.map((s) => parseInt(s.done)).includes(0)) {
                    let progressDialog = new TutorialDialog({
                        slides: slides,
                    });
                    $('.user-progress').removeClass('hide');
                    $('.user-progress .dropdown-toggle').on('click', () => {
                        progressDialog.getAndUpdateProgressState();
                        progressDialog.show();
                    });

                    if (cint(frappe.boot.sysdefaults.is_first_startup)) {
                        progressDialog.show();
                        frappe.call({
                            method: 'frappe.desk.page.setup_wizard.setup_wizard.reset_is_first_startup',
                            args: {},
                            callback: () => {},
                        });
                    }
                }
            }
        },
        freeze: false,
    });
};

let TutorialSlide = class UserProgressSlide extends frappe.ui.Slide {
    /** constructor
     * @param {dict} slide
     */
    constructor(slide = null) {
        super(slide);
    }

    /** make */
    make() {
        if (this.before_load) {
             this.before_load(this);
        }

        this.$body = $(`<div class="slide-body">
            <div class="content text-center">
                <p class="title lead">${this.title}</p>
            </div>
            <div class="form-wrapper">
                <div class="form"></div>
                <div class="add-more text-center" style="margin-top: 5px;">
                    <a class="form-more-btn hide btn btn-default btn-xs">Add More</a>
                </div>
            </div>
        </div>`).appendTo(this.$wrapper);

        this.$content = this.$body.find('.content');
        this.$form = this.$body.find('.form');
        this.$primary_btn = this.slides_footer.find('.primary');

        if (this.help) {
            this.$content.append($(`<div class="slide-help">${this.help}</div>`));
        }
        if (this.image_src) {
            this.$content.append($(`<img src="${this.image_src}" style="margin: 20px;">`));
        }
        this.reqd_fields = [];

        this.refresh();
        this.made = true;
    }

    /** setup done state */
    setup_done_state() {
        this.$body.find('.slide-help').hide();
        this.$body.find('.form-wrapper').hide();
        this.slides_footer.find('.next-btn').addClass('btn-primary');
        this.slides_footer.find('.done-btn').hide();
        this.$primary_btn.hide();
        this.make_done_state();
    }

    /** make done state */
    make_done_state() {
        this.$done_state = $(`<div class="done-state text-center">
            <div class="check-container"><i class="check fa fa-fw fa-check-circle text-success"></i></div>
            <h1 class="title"><a></a></h1>
            <div class="help-links"></div>
        </div>`).appendTo(this.$body);

        this.$done_state_title = this.$done_state.find('.title');
        this.$check = this.$done_state.find('.check');
        this.$help_links = this.$done_state.find('.help-links');

        if (this.done_state_title) {
            $('<a>' + this.done_state_title + '</a>').appendTo(this.$done_state_title);
            this.$done_state_title.on('click', () => {
                frappe.set_route(this.done_state_title_route);
            });
        }

        if (this.help_links) {
            this.help_links.map((link) => {
                let $link = $(`<a target="_blank" class="small text-muted">${link.label}</a>`);
                if (link.url) {
                    $link.attr({'href': link.url});
                } else if (link.video_id) {
                    $link.on('click', () => {
                        frappe.help.show_video(link.video_id, link.label);
                    });
                }
                this.$help_links.append($link);
            });
        }
    }

    /** before show */
    before_show() {
        if (this.done) {
            this.slides_footer.find('.next-btn').addClass('btn-primary');
            this.slides_footer.find('.done-btn').hide();
        } else {
            this.slides_footer.find('.next-btn').removeClass('btn-primary');
            this.slides_footer.find('.done-btn').show();
        }
        if (this.dialog_dismissed) {
            this.slides_footer.find('.next-btn').removeClass('btn-primary');
        }
    }

    /** primary action */
    primary_action() {
        console.log('halololo');
        console.log(this.action_name);
        this.$wrapper.parents('div.modal-dialog').find('.btn-modal-close').trigger('click');
        localStorage.tutorialListId = 0;
        localStorage.tutorialActionName = this.action_name;
        loadTippy();
    }
};

let TutorialDialog = class UserProgressDialog {
    /** constructor
     * @param {dict} slides
     */
    constructor({slides = []}) {
        this.slides = slides;
        this.progress_state_dict = {};
        this.slides.map((slide) => {
            this.progress_state_dict[slide.action_name] = slide.done || 0;
        });
        this.progress_percent = 0;
        this.setup();
    }

    /** setup */
    setup() {
        this.dialog = new frappe.ui.Dialog({title: __('Complete Setup')});
        this.$wrapper = $(this.dialog.$wrapper)
            .addClass('user-progress-dialog');
        this.slide_container = new TutorialSlides({
            parent: this.dialog.body,
            slides: this.slides,
            slide_class: TutorialSlide,
            done_state: 1,
            before_load: ($footer) => {
                $footer.find('.text-right')
                    .prepend($(`<a class="done-btn btn btn-default btn-sm">
                    ${__('Mark as Done')}</a>`))
                    .append($(`<a class="make-btn btn btn-primary btn-sm primary action">
                    ${__('Start')}</a>`));
            },
            on_update: (completed, total) => {
                let percent = completed * 100 / total;
                $('.user-progress .progress-bar').css({'width': percent + '%'});
                if (percent === 100) {
                    this.dismissProgress();
                }
            }
        });

        this.$wrapper.find('.done-btn').on('click', () => {
            this.markAsDone();
        });

        this.getAndUpdateProgressState();
        this.checkForUpdates();
    }

    /** mark as done */
    markAsDone() {
        let currentSlide = this.slide_container.current_slide;
        frappe.call({
            method: currentSlide.mark_as_done_method,
            args: {action_name: currentSlide.action_name},
            callback: function() {
                currentSlide.done = 1;
                currentSlide.refresh();
            },
            freeze: true,
        });
    }

    /** check for updates */
    checkForUpdates() {
        this.updater = setInterval(() => {
            this.getAndUpdateProgressState();
        }, 60000);
    }

    /** get and update progress state */
    getAndUpdateProgressState() {
        let me = this;
        frappe.call({
            method: 'frappe.desk.user_progress.update_and_get_user_progress',
            callback: function(r) {
                let states = r.message;
                let changed = 0;
                let completed = 0;
                Object.keys(states).map((action_name) => {
                    if (states[action_name]) {
                        completed ++;
                    }
                    if (me.progress_state_dict[action_name] != states[action_name]) {
                        changed = 1;
                        me.progress_state_dict[action_name] = states[action_name];
                    }
                });

                if (changed) {
                    Object.keys(me.slide_container.slide_dict).map((id) => {
                        let slide = me.slide_container.slide_dict[id];
                        if (me.progress_state_dict[slide.action_name]) {
                            if (!slide.done) {
                                slide.done = 1;
                                slide.refresh();
                            }
                        }
                    });
                }

                me.progress_percent = completed / Object.keys(states).length * 100;
                me.updateProgress();
            },
            freeze: false,
        });
    }

    /** update progress */
    updateProgress() {
        $('.user-progress .progress-bar').css({'width': this.progress_percent + '%'});
        if (this.progress_percent === 100) {
            this.dismissProgress();
        }
    }

    /** dismiss progress */
    dismissProgress() {
        $('.user-progress').addClass('hide');
        clearInterval(this.updater);
    }

    /** show dialog */
    show() {
        this.dialog.show();
    }
};

let TutorialSlides = class UserProgressSlides extends frappe.ui.Slides {
    /** make prev next buttons */
    make_prev_next_buttons() {
        $(`<div class="row">
            <div class="col-sm-4">
                <a class="prev-btn btn btn-default btn-sm" tabindex="0">Previous</a>
                <a class="next-btn btn btn-default btn-sm" tabindex="0">Next</a>
            </div>
            <div class="col-sm-8 text-right">
            </div>
        </div>`).appendTo(this.$footer);

        this.$prev_btn = this.$footer.find('.prev-btn').attr('tabIndex', 0)
            .on('click', () => {
                this.show_slide(this.current_id - 1);
            });

        this.$next_btn = this.$footer.find('.next-btn').attr('tabIndex', 0)
            .on('click', () => {
                if (!this.unidirectional || (this.unidirectional && this.current_slide.set_values())) {
                    this.show_slide(this.current_id + 1);
                }
            });
    }
};
