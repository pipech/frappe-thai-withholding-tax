let listId = 0;

let loaded = false;

$(document).on('page-change', () => {
    loadTippy();
});

/** load tippy yeah */
function loadTippy() {
    // don't load if id is more than list lenght
    if (tutorialList.length - 1 >= listId) {
        let tutorial = tutorialList[listId];

        // prevent setInterval multiple times
        let pageLabel = cur_page.page.label;
        if (loaded === false) {
            if (pageLabel === tutorial.pageLabel) {
                loaded = true;

                // since frappe doesn't have event when page is done loading
                // using setInterval is a way to do that
                let checkLoaded = setInterval(() => {
                    let tippyElement;
                    tippyElement = $(tutorial.tippyElement)[0];
                    if (tippyElement) {
                        // stop interval & init tippy
                        clearInterval(checkLoaded);
                        tippy(
                            tippyElement,
                            {
                                content: tutorial.content,
                                arrow: true,
                                showOnInit: true,
                                trigger: 'manual',
                                hideOnClick: 'false',
                                placement: 'top',
                                size: 'large',
                                // theme: 'light',
                            }
                        );
                        let tipEle = tippyElement._tippy;

                        // focus is event is trigger before click event
                        // when element get focus id++ and destroy tippy
                        $(tippyElement).on('focus', () => {
                            tipEle.destroy();
                            $(tippyElement).unbind('focus');
                            loaded = false;
                            listId++;
                            loadTippy();
                        });
                    }
                }, 200);
            }
        }
    }
}
