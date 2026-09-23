"use strict";

/*
    DOM
*/

const recipeCards = document.querySelectorAll(".recipe-card");

const wishlistButtons = document.querySelectorAll(".recipe-card__wishlist");

const recipeImages = document.querySelectorAll(".recipe-card__image img");

const primaryButtons = document.querySelectorAll(".btn-primary");

const outlineButtons = document.querySelectorAll(".btn-outline");


/*
    WISHLIST
*/

wishlistButtons.forEach(button=>{

    button.addEventListener("click",(e)=>{

        e.preventDefault();

        button.classList.toggle("active");

        if(button.classList.contains("active")){

            button.innerHTML="❤";

        }

        else{

            button.innerHTML="♡";

        }

    });

});


/*
    RIPPLE EFFECT
*/

function rippleEffect(event){

    const button=event.currentTarget;

    const circle=document.createElement("span");

    const diameter=Math.max(button.clientWidth,button.clientHeight);

    const radius=diameter/2;

    circle.style.width=`${diameter}px`;

    circle.style.height=`${diameter}px`;

    circle.style.left=`${event.clientX-button.offsetLeft-radius}px`;

    circle.style.top=`${event.clientY-button.offsetTop-radius}px`;

    circle.classList.add("ripple");

    const ripple=button.querySelector(".ripple");

    if(ripple){

        ripple.remove();

    }

    button.appendChild(circle);

}

primaryButtons.forEach(btn=>{

    btn.addEventListener("click",rippleEffect);

});

outlineButtons.forEach(btn=>{

    btn.addEventListener("click",rippleEffect);

});


/*
    IMAGE LOADING
*/

recipeImages.forEach(img=>{

    img.addEventListener("load",()=>{

        img.classList.add("loaded");

    });

});


/*
    INTERSECTION OBSERVER
*/

const observer=new IntersectionObserver((entries)=>{

    entries.forEach(entry=>{

        if(entry.isIntersecting){

            entry.target.classList.add("show");

            observer.unobserve(entry.target);

        }

    });

},{
    threshold:.2
});

recipeCards.forEach(card=>{

    observer.observe(card);

});


/*
    3D TILT EFFECT
*/

recipeCards.forEach(card=>{

    card.addEventListener("mousemove",(e)=>{

        const rect=card.getBoundingClientRect();

        const x=e.clientX-rect.left;

        const y=e.clientY-rect.top;

        const rotateY=((x/rect.width)-0.5)*16;

        const rotateX=((y/rect.height)-0.5)*-16;

        card.style.transform=
        `perspective(1000px)
        rotateX(${rotateX}deg)
        rotateY(${rotateY}deg)
        translateY(-12px)`;

    });

    card.addEventListener("mouseleave",()=>{

        card.style.transform="";

    });

});


/*
    PARALLAX IMAGE
*/

window.addEventListener("scroll",()=>{

    const scroll=window.pageYOffset;

    recipeImages.forEach(image=>{

        image.style.transform=
        `translateY(${scroll*0.03}px) scale(1.08)`;

    });

});


/*
    CARD GLOW
*/

recipeCards.forEach(card=>{

    card.addEventListener("mouseenter",()=>{

        card.style.boxShadow=
        "0 40px 80px rgba(34,197,94,.18)";

    });

    card.addEventListener("mouseleave",()=>{

        card.style.boxShadow="";

    });

});


/*
    BUTTON HOVER SOUND (OPTIONAL)
*/

// const audio=new Audio("/static/audio/hover.mp3");

// primaryButtons.forEach(btn=>{

// btn.addEventListener("mouseenter",()=>{

// audio.play();

// });

// });


/*
    COUNTER
*/

const counter=document.querySelector(".recipe-count");

if(counter){

    let value=0;

    const interval=setInterval(()=>{

        value++;

        counter.innerHTML=value;

        if(value>=recipeCards.length){

            clearInterval(interval);

        }

    },120);

}


/*
    CONSOLE
*/

console.log("Featured Recipes Loaded Successfully");