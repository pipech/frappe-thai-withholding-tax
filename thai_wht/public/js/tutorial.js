localStorage.tutorialLoaded = 'false';
localStorage.tutorialActionName = '';

$(document).on('page-change', () => {
    if (localStorage.tutorialActionName) {
        loadTippy();
    }
});

/** load tippy yeah */
function loadTippy() {
    // load if there is localStorage.tutorialActionName
    if (localStorage.tutorialActionName) {
        let tutorialList = tutorialDict[localStorage.tutorialActionName];

        // don't load if id is more than list lenght
        let listId = localStorage.tutorialListId;
        if (tutorialList.length - 1 >= listId) {
            let tutorial = tutorialList[listId];

            // prevent setInterval multiple times
            let pageLabel = cur_page.page.label;
            if (localStorage.tutorialLoaded === 'false') {
                if (pageLabel === tutorial.pageLabel) {
                    localStorage.tutorialLoaded = 'true';

                    // set selection prefix
                    let selPrefix;
                    if (/body.*/g.test(tutorial.tippyElement)) {
                        selPrefix = '';
                    } else if (/^li.*/g.test(tutorial.tippyElement)) {
                        selPrefix = 'div.main-section div.navbar ';
                    } else if (/navbar/g.test(tutorial.tippyElement)) {
                        selPrefix = 'div.main-section div.navbar ';
                    } else if (pageLabel === 'Desktop' || pageLabel === 'Modules') {
                        selPrefix = 'div[data-page-route="' +
                        pageLabel.toLowerCase() +
                        '"] ';
                    } else if (pageLabel === 'Delete transaction') {
                        selPrefix = 'div[data-page-route="delete_transaction"] ';
                    } else {
                        selPrefix = 'div[data-page-route="' +
                        pageLabel +
                        '"] ';
                    }

                    // since frappe doesn't have event when page is done loading
                    // using setInterval is a way to do that
                    let checkLoaded = setInterval(() => {
                        let eleSelector = selPrefix + tutorial.tippyElement;
                        let tippyElement = $(eleSelector);
                        if (tippyElement[0]) {
                            // stop interval
                            clearInterval(checkLoaded);
                            // waiting element to load
                            setTimeout(()=>{
                                if (tutorial.placement) {
                                    initTippy(
                                        tippyElement,
                                        tutorial.content,
                                        tutorial.placement
                                        );
                                } else {
                                    initTippy(tippyElement, tutorial.content);
                                }
                            }, 200);
                        }
                    }, 200);
                }
            }
        }
    }
}

/** init tippy 
 * @param {string} tippyElement
 * @param {string} content
 * @param {string} placement
*/
function initTippy(tippyElement, content, placement='bottom') {
    tippy(
        tippyElement[0],
        {
            content: content,
            arrow: true,
            showOnInit: true,
            trigger: 'manual',
            hideOnClick: 'false',
            placement: placement,
            size: 'large',
            theme: 'red',
        }
    );
    let tipEle = tippyElement[0]._tippy;

    // blur pre-selected input box on form page
    setTimeout(() => {
        tippyElement.blur();
    }, 500);

    let bindEvent = (event) => {
        tippyElement.on(event, () => {
            tippyElement.unbind(event);
            tipEle.destroy();
            localStorage.tutorialLoaded = 'false';
            localStorage.tutorialListId++;
            loadTippy();
        });
        $(document).on('page-change', () => {
            tippyElement.unbind(event);
            tipEle.destroy();
        });
    };

    let tippyEvent;

    // bind event to destroy tippy and load next one
    if (/awesomplete/g.test(tippyElement.selector)) {
        tippyEvent = 'awesomplete-selectcomplete';

        tippyElement.on('focus', () => {
            tippyElement.unbind(event);
            tipEle.destroy();
        });
        tippyElement.on(tippyEvent, () => {
            localStorage.tutorialLoaded = 'false';
            localStorage.tutorialListId++;
            loadTippy();
        });
        $(document).on('page-change', () => {
            tippyElement.unbind(tippyEvent);
            tippyElement.unbind('focus');
            tipEle.destroy();
        });
    } else if (/div.list-items/g.test(tippyElement.selector)) {
        tippyElement.closest('div.list-item-container').on('click', () => {
            tippyElement.unbind(event);
            tipEle.destroy();
            localStorage.tutorialLoaded = 'false';
            localStorage.tutorialListId++;
            loadTippy();
        });
        $(document).on('page-change', () => {
            tippyElement.unbind(event);
            tipEle.destroy();
        });
    } else {
        tippyEvent = 'focus';
        bindEvent(tippyEvent);
    }

}
