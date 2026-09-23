/*=========================================
=         HERO SECTION JAVASCRIPT         =
=========================================*/

document.addEventListener("DOMContentLoaded", () => {

    initCounterAnimation();
    initRevealAnimation();
    initParallaxEffect();
    initButtonRipple();
    initMouseGlow();

});


/*=========================================
=          COUNTER ANIMATION              =
=========================================*/

function initCounterAnimation(){

    const stats = document.querySelectorAll(".stat h2");

    const observer = new IntersectionObserver((entries)=>{

        entries.forEach(entry=>{

            if(!entry.isIntersecting) return;

            animateCounter(entry.target);

            observer.unobserve(entry.target);

        });

    },{
        threshold:.5
    });

    stats.forEach(stat=>observer.observe(stat));

}

function animateCounter(element){

    const target = parseInt(element.textContent.replace(/\D/g,""));

    const suffix = element.textContent.replace(/[0-9]/g,"");

    let current = 0;

    const increment = Math.ceil(target / 80);

    const timer = setInterval(()=>{

        current += increment;

        if(current >= target){

            current = target;

            clearInterval(timer);

        }

        element.textContent = current + suffix;

    },20);

}


/*=========================================
=          SCROLL REVEAL                  =
=========================================*/

function initRevealAnimation(){

    const elements = document.querySelectorAll(

        ".hero__badge,.hero__title,.hero__description,.hero__buttons,.hero__stats,.hero__image"

    );

    elements.forEach(el=>{

        el.style.opacity="0";

        el.style.transform="translateY(60px)";

    });

    const observer = new IntersectionObserver((entries)=>{

        entries.forEach(entry=>{

            if(entry.isIntersecting){

                entry.target.style.transition="all .8s ease";

                entry.target.style.opacity="1";

                entry.target.style.transform="translateY(0)";

            }

        });

    },{
        threshold:.2
    });

    elements.forEach(el=>observer.observe(el));

}


/*=========================================
=          PARALLAX EFFECT                =
=========================================*/

function initParallaxEffect(){

    const hero = document.querySelector(".hero");

    const image = document.querySelector(".hero__main-image");

    const cards = document.querySelectorAll(".floating-card");

    hero.addEventListener("mousemove",(e)=>{

        const x = (window.innerWidth/2 - e.clientX)/35;

        const y = (window.innerHeight/2 - e.clientY)/35;

        image.style.transform = `translate(${x}px,${y}px)`;

        cards.forEach((card,index)=>{

            const speed = (index+1)*8;

            card.style.transform = `translate(${x/speed}px,${y/speed}px)`;

        });

    });

    hero.addEventListener("mouseleave",()=>{

        image.style.transform="translate(0,0)";

        cards.forEach(card=>{

            card.style.transform="translate(0,0)";

        });

    });

}


/*=========================================
=            BUTTON RIPPLE               =
=========================================*/

function initButtonRipple(){

    const buttons=document.querySelectorAll(".btn");

    buttons.forEach(btn=>{

        btn.addEventListener("click",(e)=>{

            const ripple=document.createElement("span");

            const rect=btn.getBoundingClientRect();

            const size=Math.max(rect.width,rect.height);

            ripple.style.width=size+"px";

            ripple.style.height=size+"px";

            ripple.style.left=e.clientX-rect.left-size/2+"px";

            ripple.style.top=e.clientY-rect.top-size/2+"px";

            ripple.classList.add("ripple");

            btn.appendChild(ripple);

            setTimeout(()=>{

                ripple.remove();

            },700);

        });

    });

}


/*=========================================
=          MOUSE GLOW EFFECT             =
=========================================*/

function initMouseGlow(){

    const hero=document.querySelector(".hero");

    const glow=document.createElement("div");

    glow.className="mouse-glow";

    hero.appendChild(glow);

    hero.addEventListener("mousemove",(e)=>{

        const rect=hero.getBoundingClientRect();

        glow.style.left=e.clientX-rect.left+"px";

        glow.style.top=e.clientY-rect.top+"px";

    });

}


/*=========================================
=      OPTIONAL SMOOTH SCROLL            =
=========================================*/

document.querySelectorAll('a[href^="#"]').forEach(link=>{

    link.addEventListener("click",(e)=>{

        const id=link.getAttribute("href");

        if(id==="#") return;

        e.preventDefault();

        const target=document.querySelector(id);

        if(target){

            target.scrollIntoView({

                behavior:"smooth",

                block:"start"

            });

        }

    });

});