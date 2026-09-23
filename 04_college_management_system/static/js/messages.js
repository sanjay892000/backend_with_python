document.addEventListener("DOMContentLoaded", () => {

    const toasts = document.querySelectorAll(".toast");

    toasts.forEach((toast) => {

        setTimeout(() => {

            toast.classList.add(
                "opacity-0",
                "translate-x-10"
            );

            setTimeout(() => {

                toast.remove();

            }, 400);

        }, 5000);

    });

    document.querySelectorAll(".close-toast")
        .forEach(button => {

            button.addEventListener("click", () => {

                button.closest(".toast").remove();

            });

        });

});