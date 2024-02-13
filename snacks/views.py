from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["snacks"] = [
            {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/French_Fries.JPG/250px-French_Fries.JPG",
                "title": "French Fries",
                "description": "French fries, or simply fries, are pieces of potato that have been deep-fried.",
                "reference_url": "https://en.wikipedia.org/wiki/French_fries"
            },
            {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Khaep_mu.jpg/220px-Khaep_mu.jpg",
                "title": "Pork Rind",
                "description": "Pork rind is the culinary term for the skin of a pig. It can be used in many different ways.",
                "reference_url": "https://en.wikipedia.org/wiki/Pork_rind"
            },
            {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/BrezelnSalz02_%28cropped%29.JPG/250px-BrezelnSalz02_%28cropped%29.JPG",
                "title": "Pretzel",
                "description": "A pretzel is a type of baked bread product made from dough most commonly shaped into a twisted knot.",
                "reference_url": "https://en.wikipedia.org/wiki/Pretzel"
            }
        ]

        return context


class AboutPageView(TemplateView):
    template_name = 'about.html'