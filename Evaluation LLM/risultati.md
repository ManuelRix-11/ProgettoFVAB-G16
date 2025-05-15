## Evaluation QA
Per la evaluation nel lato QA e' stata scelta come metrica di valutazione il [BertScore](https://huggingface.co/spaces/evaluate-metric/bertscore).

BERTScore è una metrica che misura la qualità delle risposte o delle generazioni di testo utilizzando i vettori di 
rappresentazione del linguaggio per calcolare la similarità tra il testo prodotto e il testo di riferimento.

### Configurazione di evaluation
Tutte le configurazioni di tutti i modelli sono stati effettuati con le stesse condizioni e parametri 
(Eccetto i max-token che variano da modello a modello).

- temperature: 0.7
- top_p: 1
- prompt : tutti i prompt sono presenti nel file qa_dataset.json

## Evaluation di generazione di dati sintetici
Per questo tipo di evaluation e' stata scelta come metrica di valutazione, una metrica utilizzata per il confronto delle
distribuzioni in statistica, la KS-statistic (Kolmogorov-Smirnov statistic).

Quando applicata alla valutazione di dati sintetici, viene utilizzata per confrontare la 
distribuzione statistica tra i dati generati e i dati reali

# Tabella risultati
| Modello | Run Locale | Run as Service | Evaluation QA (Local) | Evaluation QA (Service) | Evaluation SynGen (TDB) |
|--------|:----------:|:--------------:|:---------------------:|:-----------------------:|:-----------------------:|
| gemma2:9b |     ✅      |       ✅        |         ≈72%          |          ≈80%           |                         |
| qwen2.5:3b |     ✅      |       ❌        |         ≈73%          |            ❌            |                         |
| llama3.2:latest |     ✅      |       ❌         |         ≈72%          |              ❌           |                         |
| llama-3.3-70b-versatile |     ❌      |       ✅        |           ❌            |          ≈80%           |                         |
| llama-3.1-8b-instant |     ❌      |       ✅        |           ❌            |          ≈75%           |                         |
| pixtral-12b-2409 |     ❌      |       ✅        |           ❌            |          ≈80%           |                         |
| open-mixtral-8x7b |     ❌      |       ✅        |           ❌            |          ≈75%           |                         |
| mistral-small-2503 |     ❌      |       ✅        |           ❌            |          ≈77%           |                         |
| mistral-large-2411 |     ❌      |       ✅        |           ❌            |          ≈75%           |                         |


## Possibili cambiamenti o miglioramenti
- [ ] Aggiunta della parte di valutazione della generazione di dati sintetici;
- [ ] Rieffettuare i test con parametri di temperature e top_p diversi;
- [ ] Provare modelli fine-tuned nel dominio di riferimento;
- [ ] Utilizzare diversi metodi di prompt-engineering, presenti anche nello stato dell'arte

## Problematiche riscontrate
- Potenza hardware delle run locali limitata
- Servizi in grado di ospitare modelli (e quindi di rispondere a richieste) spesso sono limitati nelle versioni gratuite o
direttamente a pagamento
