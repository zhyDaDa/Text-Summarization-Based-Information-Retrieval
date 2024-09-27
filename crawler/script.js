(async () => {
    let aaa = [];

    const f = async () => {
        let ttt = [];
        await new Promise((resolve) => setTimeout(resolve, 100));
        document.querySelectorAll(".r-image-desc").forEach(function (el) {
            let t = el.innerText;
            ttt.push(t);
        });
        return ttt;
    };
    let bu = document.querySelectorAll("button.page-link");
    bu = bu[bu.length - 1];

    // 逐个点击按钮, 确保f执行完毕后再点击下一个按钮
    const g = async (i) => {
        console.log(i);
        if (i < 0) {
            return;
        }
        let ttt = await f();
        aaa = aaa.concat(ttt);
        bu.click();
        await g(i-1);
    };

    await g(60);
    // 去重
    let bbb = [...new Set(aaa)];
    console.log(bbb);

})();
