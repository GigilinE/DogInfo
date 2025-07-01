# Istruzioni per l'Azione del Server Odoo

## Come Utilizzare lo Script

### 1. Accesso alle Azioni del Server
1. Accedi al tuo sistema Odoo
2. Vai a **Impostazioni** (Settings)
3. Clicca su **Tecnico** nel menu laterale
4. Seleziona **Azioni del Server** (Server Actions)

### 2. Creazione dell'Azione del Server
1. Clicca su **Crea** (Create)
2. Compila i campi:
   - **Nome dell'azione**: "Verifica e Crea Campi Cane"
   - **Modello**: Seleziona "res.partner" (Contatto)
   - **Tipo di azione**: Seleziona "Esegui codice Python"

### 3. Inserimento del Codice
Copia e incolla il contenuto del file `server_action_simplified.py` nel campo **Codice Python**.

### 4. Esecuzione
1. Salva l'azione
2. Clicca su **Esegui** (Run)
3. Vedrai un popup con i risultati dell'operazione

## Cosa Fa lo Script

### Verifiche Eseguite:
1. **Controlla** se il modulo `dog_registration` è installato
2. **Verifica** l'esistenza dei campi:
   - `x_dog_name` (Nome del Cane)
   - `x_dog_breed` (Razza del Cane) 
   - `x_dog_age` (Età del Cane)
   - `x_dog_weight` (Peso del Cane)

### Azioni Eseguite:
1. **Crea automaticamente** i campi mancanti nel modello `res.partner`
2. **Mostra lo stato** di ogni campo (esistente, creato, errore)
3. **Fornisce istruzioni** per i prossimi passi

## Personalizzazione dei Form

### A. Form di Registrazione (Signup)

**Metodo 1 - Tramite Editor del Sito Web:**
1. Vai a **Sito web** > **Configurazione** > **Personalizza**
2. Attiva la modalità sviluppatore
3. Trova il template di signup
4. Aggiungi i campi HTML per i dati del cane

**Metodo 2 - Tramite File XML:**
Modifica il file `views/auth_signup_views.xml` nel modulo `dog_registration`

### B. Form del Portale Utente

**Metodo 1 - Tramite Editor del Sito Web:**
1. Vai a **Sito web** > **Configurazione** > **Personalizza**
2. Trova il template "My Account" o "I miei dettagli"
3. Aggiungi i campi per i dati del cane

**Metodo 2 - Tramite File XML:**
Modifica il file `views/portal_views.xml` nel modulo `dog_registration`

## Esempio di Codice HTML per i Form

### Per il Form di Registrazione:
```html
<div class="form-group">
    <label for="x_dog_name">Nome del Cane</label>
    <input type="text" name="x_dog_name" id="x_dog_name" class="form-control"/>
</div>
<div class="form-group">
    <label for="x_dog_breed">Razza del Cane</label>
    <input type="text" name="x_dog_breed" id="x_dog_breed" class="form-control"/>
</div>
<div class="form-group">
    <label for="x_dog_age">Età del Cane</label>
    <input type="number" name="x_dog_age" id="x_dog_age" class="form-control"/>
</div>
<div class="form-group">
    <label for="x_dog_weight">Peso del Cane (kg)</label>
    <input type="number" step="0.01" name="x_dog_weight" id="x_dog_weight" class="form-control"/>
</div>
```

### Per il Form del Portale:
```html
<div class="form-group col-xl-6">
    <label class="col-form-label" for="x_dog_name">Nome del Cane</label>
    <input type="text" name="x_dog_name" class="form-control"
           t-att-value="partner.x_dog_name"/>
</div>
<div class="form-group col-xl-6">
    <label class="col-form-label" for="x_dog_breed">Razza del Cane</label>
    <input type="text" name="x_dog_breed" class="form-control"
           t-att-value="partner.x_dog_breed"/>
</div>
<div class="form-group col-xl-6">
    <label class="col-form-label" for="x_dog_age">Età del Cane</label>
    <input type="number" name="x_dog_age" class="form-control"
           t-att-value="partner.x_dog_age"/>
</div>
<div class="form-group col-xl-6">
    <label class="col-form-label" for="x_dog_weight">Peso del Cane (kg)</label>
    <input type="number" step="0.01" name="x_dog_weight" class="form-control"
           t-att-value="partner.x_dog_weight"/>
</div>
```

## Aggiornamento dei Controller

Dopo aver creato i campi, assicurati che i controller li gestiscano:

1. **Auth Signup Controller** (`controllers/auth_signup.py`)
2. **Portal Controller** (`controllers/portal.py`)

Questi dovrebbero già essere configurati se il modulo `dog_registration` è installato correttamente.

## Troubleshooting

### Errori Comuni:
1. **Campo già esistente**: Normale, lo script lo rileva e salta la creazione
2. **Errore di permessi**: Assicurati di essere amministratore
3. **Modello non trovato**: Verifica che stai usando il modello corretto

### Verifica Risultati:
1. Vai a **Impostazioni** > **Tecnico** > **Struttura Database** > **Campi**
2. Filtra per modello `res.partner`
3. Cerca i campi `x_dog_*`

## Note Importanti

- I campi creati sono di tipo "manuale" e non vengono persi negli aggiornamenti
- Puoi eseguire lo script più volte senza problemi
- I campi esistenti non vengono modificati o duplicati
- Lo script è sicuro e non modifica dati esistenti