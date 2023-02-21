// Javascript to run animations when they are taken into view. Slight delay to account for page load time.

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function animateOnVis() {

    var revealsF = document.querySelectorAll(".fadeInVis");
    var revealsT = document.querySelectorAll(".typedOutText");
    revealsT[0].classList.add("active");


    for (var i = 0; i < revealsF.length; i++) {

        var windowHeightF = window.innerHeight;
        var elementTopF = revealsF[i].getBoundingClientRect().top;
        var elementVisibleF = 150;

        if (elementTopF < windowHeightF - elementVisibleF) {

            revealsF[i].classList.add("active");

        }
    }
}

window.addEventListener("scroll", animateOnVis);

sleep(75).then(() => {

    animateOnVis()

});








