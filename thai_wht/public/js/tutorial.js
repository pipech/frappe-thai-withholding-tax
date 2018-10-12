let listId = 0;
let loaded = false;
// temporary
tutorialList = tutorialList[2].lessonList;

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

                    // set selection prefix
                    let selPrefix;
                    if (/body.*/g.test(tutorial.tippyElement)) {
                        selPrefix = '';
                    } else if (/^li.*/g.test(tutorial.tippyElement)) {
                        selPrefix = 'div.main-section div.navbar ';
                    } else if (pageLabel === 'Desktop' || pageLabel === 'Modules') {
                        selPrefix = 'div[data-page-route="' +
                        pageLabel.toLowerCase() +
                        '"] ';
                    } else {
                        selPrefix = 'div[data-page-route="' +
                        pageLabel +
                        '"] ';
                    }

                    // select element
                    let eleSelector = selPrefix + tutorial.tippyElement;
                    let tippyElement;
                    tippyElement = $(eleSelector)[0];

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
                        // blur pre-selected input box on form page
                        setTimeout(() => {
                            $(tippyElement).blur();
                        }, 500);
                    }
                }, 200);
            }
        }
    }
}
