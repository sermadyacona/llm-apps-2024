# Tillämpad AI 2024

![Wanna chat](images/llm-apps-2024.png)

# Välkommen till Tillämpad AI 2024!

## Agenda
Finns här: [AGENDA.md](AGENDA.md)


## Sätt upp din utvecklingsmiljö


### GitHub Codespaces
* Skapa först en Fork av detta repository (mest för om man vill kunna spara/committa ändringar)
* Klicka sedan på "Code" och "Create codespace on main"

### Juptyer Notebooks i Google Colab

#### Sätt upp API-nycklar mm

Under "Hemligheter" / "Secrets" i vänstermenyn kan du konfigurera API-nycklar och andra känsliga uppgifter. 
![Google Colab - Hemligheter](images/colab-keys.png)

Dessa kan du sedan använda i dina notebooks på detta sätt:
![Google Colab - Hemligheter](images/colab-keys.png)


#### Notebooks för kursen...
...finns på [**Google Drive**](https://drive.google.com/file/d/1Rd_Ri_YRft7ojLBXet5temLtqzChamiX/view?usp=sharing)



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


## Bra länkar

### Microsoft OpenAI
* [Azure OpenAI Service documentation - Quickstarts, Tutorials, API Reference - Azure AI services](https://learn.microsoft.com/en-us/azure/ai-services/openai/)

### LangChain cheatsheet
![lc-cheatsheet.png](images/lc-cheatsheet.png)
* https://python.langchain.com/docs/how_to/lcel_cheatsheet/


### LangChain
* [How-to guides](https://python.langchain.com/docs/how_to/)
* [Tutorials](https://python.langchain.com/docs/tutorials/)
* Cookbook: [langchain/cookbook at master · langchain-ai/langchain](https://github.com/langchain-ai/langchain/tree/master/cookbook)
* Prompt hub: https://smith.langchain.com/hub
* Project templates (trasig?): https://templates.langchain.com/trending

### LangGraph
* Exempel / cookbook: https://github.com/langchain-ai/langgraph/tree/main/examples

### Övrigt
**Nir Diamante**
* https://github.com/NirDiamant/GenAI_Agents
* https://github.com/NirDiamant/RAG_Techniques
* https://github.com/NirDiamant/Prompt_Engineering

**5_Levels_Of_Text_Splitting**
* [RetrievalTutorials/tutorials/LevelsOfTextSplitting/5_Levels_Of_Text_Splitting.ipynb at main · FullStackRetrieval-com/RetrievalTutorials](https://github.com/FullStackRetrieval-com/RetrievalTutorials/blob/main/tutorials/LevelsOfTextSplitting/5_Levels_Of_Text_Splitting.ipynb)

