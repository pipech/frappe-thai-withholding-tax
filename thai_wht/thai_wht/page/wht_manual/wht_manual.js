let manualUrl = 'https://docs.google.com/document/d/1JhlKvOL91ht_KA9BOscLQH9U9D2rQQ-Un2R3wgZIuhA/'
let popUp = window.open(manualUrl, '_blank');

if (popUp == null || typeof(popUp)=='undefined') {
    frappe.confirm(
        'คุณต้องการเปิดคู่มือการใช้งานใช่หรือไม่ ?',
        ()=>{
            window.open(manualUrl, '_blank');
            window.location = '/desk';
        },
        ()=>{
            window.location = '/desk';
        },
    );
};

setTimeout(()=>{
    window.location = '/desk';
}, 10000);
