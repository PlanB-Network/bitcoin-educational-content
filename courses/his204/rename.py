#!/usr/bin/env python3
import re
from pathlib import Path

def main():
    # Lista delle immagini da eliminare (solo i numeri)
    images_to_remove = [
        '039', '044', '050', '052', '056', '058', '061', '063', '065', '067',
        '068', '080', '085', '087', '089', '091', '093', '095', '097', '100',
        '103', '105', '106', '108', '110', '117', '119', '121', '123', '129',
        '134', '135', '137', '138'
    ]
    
    # Trova tutti i file .md nella cartella corrente
    md_files = list(Path('.').glob('*.md'))
    
    if not md_files:
        print("Nessun file .md trovato nella cartella corrente")
        return
    
    print(f"Trovati {len(md_files)} file(i) .md\n")
    
    for md_file in md_files:
        print(f"Elaborazione: {md_file.name}")
        
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # STEP 1: Rimuovi SOLO la parte ![image](...) dalle righe, non l'intera riga
        removed_count = 0
        
        for img_num in images_to_remove:
            # Pattern per trovare ![image](assets/fr/XXX.webp) o ![...](...) varianti
            pattern = r'!\[.*?\]\(assets/fr/' + img_num + r'\.webp\)'
            matches = re.findall(pattern, content)
            if matches:
                content = re.sub(pattern, '', content)
                removed_count += len(matches)
                print(f"  Rimossa: assets/fr/{img_num}.webp")
        
        # Rimuovi righe vuote multiple consecutive create dalla rimozione
        content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
        
        # STEP 2: Trova tutte le immagini rimaste nell'ordine di apparizione
        pattern = r'!\[image\]\(assets/fr/(\d{3})\.webp\)'
        matches = list(re.finditer(pattern, content))
        
        # Crea mappatura vecchio numero -> nuovo numero
        rename_map = {}
        for idx, match in enumerate(matches, start=1):
            old_num = match.group(1)
            new_num = f'{idx:03d}'
            if old_num != new_num:
                rename_map[old_num] = new_num
        
        # STEP 3: Applica le rinominazioni
        for old_num, new_num in rename_map.items():
            old_path = f'assets/fr/{old_num}.webp'
            new_path = f'assets/fr/{new_num}.webp'
            content = content.replace(old_path, new_path)
            print(f"  Rinominata: {old_path} -> {new_path}")
        
        # Scrivi il file modificato
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  Totale rimosse: {removed_count}")
        print(f"  Totale rinominate: {len(rename_map)}\n")
    
    print(f"{'='*60}")
    print("Operazione completata!")
    print(f"{'='*60}")
    print("\nATTENZIONE: I file .md sono stati aggiornati.")
    print("Ricordati di rinominare anche i file fisici in assets/fr/")
    print("secondo la mappatura mostrata sopra!")

if __name__ == "__main__":
    main()