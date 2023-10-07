from django.shortcuts import render, redirect
from .contact_form import ContactForm

def contact_view(request):
    if request.method == "POST":  
        form = ContactForm(request.POST)  # Créez une instance du formulaire avec les données POST
        if form.is_valid():  # Vérifiez si le formulaire est valide
            form.save()  # Enregistrez les données du formulaire dans la base de données
            return redirect('/')  # Redirigez l'utilisateur vers une page de confirmation ou une autre page
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
