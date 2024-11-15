# Tillämpad AI 2024

![Wanna chat](images/llm-apps-2024.png)

# Välkommen till Tillämpad AI 2024!

## Agenda
Finns här: [AGENDA.md](AGENDA.md)


## Sätt upp din utvecklingsmiljö


### Juptyer Notebooks i Google Colab

#### Sätt upp API-nycklar mm

Under "Hemligheter" / "Secrets" i vänstermenyn kan du konfigurera API-nycklar och andra känsliga uppgifter. 
![Google Colab - Hemligheter](images/colab-keys.png)

Dessa kan du sedan använda i dina notebooks på detta sätt:
![Google Colab - Hemligheter](images/colab-keys.png)


#### Notebooks för kursen...
...finns på [**Google Drive**](https://drive.google.com/drive/folders/1CaWt7ITCTe8JzB1erMdDJW36kBpNjLyt?usp=sharing)



### Skapa en lokal Python & Jupyter miljö

1. Skapa en virtual environment för Python:
   ```sh
   python3 -m venv .venv
   ```
2. Aktivera:
   ```sh
   source .venv/bin/activate
   ```
3. Installera beroenden:
   ```sh
   pip install -r requirements.txt
   ```
   
Efter att miljön är uppsatt, behöver du bara göra steg **två (2)** varje gång du öppnar en ny terminal.


## Labbmiljö i Azure
* Resursgrupp: ai-tokyo-2024

