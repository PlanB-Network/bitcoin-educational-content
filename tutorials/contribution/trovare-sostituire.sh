#!/bin/bash

# Richiesta all'utente di inserire la parola o frase da cercare
read -p "Inserisci la parola o frase da cercare: " search_term

# Controlla se l'utente ha inserito un termine di ricerca
if [ -z "$search_term" ]; then
    echo "Nessun termine di ricerca fornito. Uscita."
    exit 1
fi

# Richiesta all'utente di inserire la parola o frase da sostituire
read -p "Inserisci la parola o frase da sostituire: " replace_term

# Controlla se l'utente ha inserito un termine di sostituzione
if [ -z "$replace_term" ]; then
    echo "Nessun termine di sostituzione fornito. Uscita."
    exit 1
fi

# Cerca e sostituisci il termine nella cartella corrente e nelle sottocartelle
echo "Cercando e sostituendo '$search_term' con '$replace_term' nella cartella corrente e nelle sottocartelle..."

# Usa sed per cercare e sostituire
find ./ -type f -exec sed -i "s/$search_term/$replace_term/g" {} +

# Controlla se la sostituzione è stata eseguita
if [ $? -eq 0 ]; then
    echo "Sostituzione completata."
else
    echo "Nessuna sostituzione effettuata."
fi
