from django.shortcuts import render

# Create your views here.
trainings = [
    {
        "id": 1,
        "title": "First Training Class",
        "image": "images/training-image-01.jpg",
        "desc": "First Class Description",
    },
    {
        "id": 2,
        "title": "Second Training Class",
        "image": "images/training-image-02.jpg",
        "desc": "Second Class Description",
    },
    {
        "id": 3,
        "title": "Third Training Class",
        "image": "images/training-image-03.jpg",
        "desc": "Third Class Description",
    },
    {
        "id": 4,
        "title": "Fourth Training Class",
        "image": "images/training-image-04.jpg",
        "desc": "Fourth Class Description",
    },
]


def home(request):
    person = {"name": "Komal", "age": 24, "add": "LKO"}
    return render(
        request, "pages/home.html", {"person": person, "title": "Testing Data"}
    )


def about(request):
    program = [
        {
            "id": 1,
            "title": "Basic Fitness",
            "description": "Build your foundation with beginner-friendly workouts, guided exercises and healthy fitness habits.",
            "icon": "images/features-first-icon.png",
            "slug": "basic-fitness",
        },
        {
            "id": 2,
            "title": "New Gym Training",
            "description": "Learn modern workout techniques with certified trainers using advanced gym equipment.",
            "icon": "images/features-first-icon.png",
            "slug": "new-gym-training",
        },
        {
            "id": 3,
            "title": "Basic Muscle Course",
            "description": "Increase muscle strength through structured weight training and nutrition guidance.",
            "icon": "images/features-first-icon.png",
            "slug": "basic-muscle-course",
        },
        {
            "id": 4,
            "title": "Advanced Muscle Course",
            "description": "Advanced strength training designed for experienced athletes and bodybuilders.",
            "icon": "images/features-first-icon.png",
            "slug": "advanced-muscle-course",
        },
        {
            "id": 5,
            "title": "Yoga Training",
            "description": "Improve flexibility, posture and mindfulness through guided yoga sessions.",
            "icon": "images/features-first-icon.png",
            "slug": "yoga-training",
        },
        {
            "id": 6,
            "title": "Body Building Course",
            "description": "Achieve maximum muscle growth with expert coaching, nutrition and progressive workout plans.",
            "icon": "images/features-first-icon.png",
            "slug": "body-building-course",
        },
    ]
    return render(request, "pages/about.html", {"program":program})


def classes(request):
    return render(
        request,
        "pages/classes.html",
        {"trainings": trainings, "selected": trainings[0]},
    )


def classes_detail(request, id):
    selected = next(item for item in trainings if item["id"] == id)

    return render(
        request, "pages/classes.html", {"trainings": trainings, "selected": selected}
    )


def schedules(request):
    return render(request, "pages/schedules.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        print(name)
        print(email)
        print(subject)
        print(message)

    return render(request, "pages/contact.html")


def login(request):
    return render(request, "pages/login.html")


def signup(request):
    return render(request, "pages/signup.html")
