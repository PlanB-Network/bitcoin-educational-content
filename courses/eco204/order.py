import re
from pathlib import Path

def renumber_images_in_file(content):
    """Rinumera tutte le immagini in ordine sequenziale partendo da 001."""
    # Pattern per trovare le immagini
    pattern = r'!\[([^\]]*)\]\(assets/fr/(\d+)\.webp\)'
    
    # Trova tutte le occorrenze con la loro posizione
    matches = list(re.finditer(pattern, content))
    
    if not matches:
        return content, 0
    
    # Crea le sostituzioni in ordine inverso per evitare problemi di offset
    replacements = []
    for idx, match in enumerate(matches, start=1):
        new_num = f"{idx:03d}"
        
        replacements.append({
            'start': match.start(),
            'end': match.end(),
            'old': match.group(0),
            'new': f"![{match.group(1)}](assets/fr/{new_num}.webp)"
        })
    
    # Applica le sostituzioni dall'ultima alla prima
    new_content = content
    for repl in reversed(replacements):
        new_content = new_content[:repl['start']] + repl['new'] + new_content[repl['end']:]
    
    return new_content, len(replacements)

def process_markdown_files(directory='.'):
    """Processa tutti i file .md nella directory."""
    md_files = sorted(Path(directory).glob('*.md'))
    
    if not md_files:
        print(f"Nessun file .md trovato nella directory {directory}")
        return
    
    print(f"Trovati {len(md_files)} file .md\n")
    
    for md_file in md_files:
        print(f"Processando: {md_file.name}")
        
        # Leggi il contenuto
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Conta le immagini originali
        original_images = re.findall(r'!\[([^\]]*)\]\(assets/fr/(\d+)\.webp\)', content)
        
        # Rinumera le immagini
        new_content, changes = renumber_images_in_file(content)
        
        if changes > 0:
            # Salva il file modificato
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"  ✓ {changes} immagini rinumerate (da 001 a {changes:03d})")
            
            # Mostra i numeri originali
            unique_originals = sorted(set(int(img[1]) for img in original_images))
            if len(unique_originals) <= 10:
                print(f"  • Numeri originali: {unique_originals}")
            else:
                print(f"  • Range originale: {min(unique_originals)} - {max(unique_originals)}")
        else:
            print(f"  → Nessuna immagine trovata")
        print()

if __name__ == "__main__":
    process_markdown_files()