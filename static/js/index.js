// file: static/js/index.js

document.addEventListener("DOMContentLoaded", function () {

    class ClickSpark extends HTMLElement {
        constructor() {
            super();
            this.attachShadow({mode: "open"});
            this.root = document.documentElement;
            this.svg;
        }

        get activeEls() {
            return this.getAttribute("active-on");
        }

        connectedCallback() {
            this.setupSpark();

            this.root.addEventListener("click", (e) => {
                if (this.activeEls && !e.target.matches(this.activeEls)) return;

                this.setSparkPosition(e);
                this.animateSpark();
            });
        }

        animateSpark() {
            let sparks = [...this.svg.children];
            let size = parseInt(sparks[0].getAttribute("y1"));
            let offset = size / 2 + "px";

            let keyframes = (i) => {
                let deg = `calc(${i} * (360deg / ${sparks.length}))`;

                return [
                    {
                        strokeDashoffset: size * 3,
                        transform: `rotate(${deg}) translateY(${offset})`
                    },
                    {
                        strokeDashoffset: size,
                        transform: `rotate(${deg}) translateY(0)`
                    }
                ];
            };

            let options = {
                duration: 660,
                easing: "cubic-bezier(0.25, 1, 0.5, 1)",
                fill: "forwards"
            };

            sparks.forEach((spark, i) => spark.animate(keyframes(i), options));
        }

        setSparkPosition(e) {
            let rect = this.root.getBoundingClientRect();

            this.svg.style.left =
                e.clientX - rect.left - this.svg.clientWidth / 2 + "px";
            this.svg.style.top =
                e.clientY - rect.top - this.svg.clientHeight / 2 + "px";
        }

        setupSpark() {
            let template = `
          <style>
            :host {
              display: contents;
            }
            
            svg {
              pointer-events: none;
              position: absolute;
              rotate: -20deg;
              stroke: var(--click-spark-color, currentcolor);
            }
    
            line {
              stroke-dasharray: 30;
              stroke-dashoffset: 30;
              transform-origin: center;
            }
          </style>
          <svg width="30" height="30" viewBox="0 0 100 100" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="4">
            ${Array.from(
                {length: 8},
                (_) => `<line x1="50" y1="30" x2="50" y2="4"/>`
            ).join("")}
          </svg>
        `;

            this.shadowRoot.innerHTML = template;
            this.svg = this.shadowRoot.querySelector("svg");
        }
    }

    customElements.define("click-spark", ClickSpark);

    // Scroll To Top
    const button = document.getElementById('back-to-top');
    const scrollTriggerHeight = 100;
    const isBehaviorSmooth = true;

    function handleScroll() {
        if (!button) return;

        if (window.innerWidth < 768 && button.dataset.hiddenMobile) return;

        if (window.scrollY > scrollTriggerHeight) {
            button.classList.add('active-progress');
        } else {
            button.classList.remove('active-progress');
        }

        const circleElement = button.querySelector('.circle');

        if (circleElement) {
            updateCircleProgress(circleElement);
        }
    }

    function updateCircleProgress(circleElement) {
        const scrollPercentage = window.scrollY / (document.body.offsetHeight - window.innerHeight);
        const rotationDegrees = 360 * scrollPercentage;
        circleElement.style.setProperty("--cricle-degrees", rotationDegrees + "deg");
    }

    function scrollToTop(event) {
        event.preventDefault();
        window.scrollTo({top: 0, behavior: isBehaviorSmooth ? 'smooth' : 'auto'});
    }

    // Attach the scroll event listener with debouncing
    let scrollTimeout = null;

    function onScroll() {
        if (scrollTimeout) {
            clearTimeout(scrollTimeout);
        }
        scrollTimeout = setTimeout(handleScroll, 10);
    }

    // Add event listeners
    window.addEventListener('scroll', onScroll);
    button.addEventListener('click', scrollToTop);

    // Initial call to handleScroll
    handleScroll();

    // Cleanup function if needed (not part of vanilla JS, but for completeness)
    function cleanup() {
        window.removeEventListener('scroll', onScroll);
        button.removeEventListener('click', scrollToTop);
    }

    // Optionally, you can call cleanup on unload if required
    window.addEventListener('unload', cleanup);


    // Handling mini cart rendering
    const cartButton = document.querySelector('.js-call-mini-cart');
    const cartElement = document.querySelector('.js-mini-cart');
    const closeMiniCartButton = document.querySelector('.js-mini-cart .close-mini-cart');

    // Add click event listener
    cartButton.addEventListener('click', function (event) {
        // Add the 'active' class to the button when clicked
        event.preventDefault();
        cartElement.classList.toggle('active');
    });

    closeMiniCartButton.addEventListener('click', function (event) {
        // Add the 'active' class to the button when clicked
        event.preventDefault();
        cartElement.classList.toggle('active');
    });

    function hexToRgb(hex) {
        var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
        return result ? {
            r: parseInt(result[1], 16),
            g: parseInt(result[2], 16),
            b: parseInt(result[3], 16)
        } : null;
    }

    var r = hexToRgb("#ffffff").r;
    var g = hexToRgb("#ffffff").g;
    var b = hexToRgb("#ffffff").b;

    document.querySelector('.header-v1-h1').style.background = 'rgba(' + r + ',' + g + ',' + b + ',1)';

    function menuDesktopScroll() {
        var nav = document.querySelector(".jsheader_sticky");
        nav.classList.remove('menu_scroll_v1');

        document.addEventListener("scroll", function () {
            var scrollTop = document.documentElement.scrollTop || document.body.scrollTop;

            if (scrollTop > nav.offsetHeight) {
                nav.classList.add('menu_scroll_v1');
            } else {
                nav.classList.remove('menu_scroll_v1');
            }

            var r = hexToRgb("#ffffff").r;
            var g = hexToRgb("#ffffff").g;
            var b = hexToRgb("#ffffff").b;

            var header = document.querySelector('.header-v1-h1.menu_scroll_v1');
            if (header) {
                header.style.background = 'rgba(' + r + ',' + g + ',' + b + ',1)';
            }
        });
    }

    menuDesktopScroll();

});
