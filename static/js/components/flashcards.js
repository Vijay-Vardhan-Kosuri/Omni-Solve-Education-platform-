/**
 * Flashcard Deck Runner Component
 */
const FlashcardComponent = {
    activeDeck: null,
    currentCardIndex: 0,
    isFlipped: false,

    init() {
        AppState.subscribe(state => this.renderDecks(state));

        const cardEl = document.getElementById('flashcardElement');
        if (cardEl) {
            cardEl.addEventListener('click', () => this.flipCard());
        }

        const prevBtn = document.getElementById('prevCardBtn');
        const nextBtn = document.getElementById('nextCardBtn');

        if (prevBtn) prevBtn.addEventListener('click', () => this.prevCard());
        if (nextBtn) nextBtn.addEventListener('click', () => this.nextCard());
    },

    renderDecks(state) {
        const container = document.getElementById('flashcardDeckContainer');
        if (!container) return;

        if (state.flashcardDecks.length === 0) {
            container.innerHTML = '<p style="color:var(--text-muted);">No flashcard decks available.</p>';
            return;
        }

        container.innerHTML = state.flashcardDecks.map(deck => `
            <div class="deck-card" onclick="FlashcardComponent.loadDeck(${deck.id})">
                <div style="font-size:0.75rem; font-weight:700; color:${deck.subject_color || '#3B82F6'};">${deck.subject_code}</div>
                <h3 style="font-size:1.1rem; color:var(--text-primary); margin:0.3rem 0;">${deck.title}</h3>
                <p style="font-size:0.8rem; color:var(--text-muted);">${deck.cards_count} Cards</p>
            </div>
        `).join('');
    },

    loadDeck(deckId) {
        const deck = AppState.flashcardDecks.find(d => d.id === deckId);
        if (!deck || deck.cards.length === 0) return;

        this.activeDeck = deck;
        this.currentCardIndex = 0;
        this.isFlipped = false;

        document.getElementById('activeFlashcardViewer').classList.remove('hidden');
        this.updateCardDisplay();
    },

    updateCardDisplay() {
        if (!this.activeDeck) return;
        const card = this.activeDeck.cards[this.currentCardIndex];

        const frontText = document.getElementById('cardFrontText');
        const backText = document.getElementById('cardBackText');
        const tracker = document.getElementById('cardProgressTracker');
        const cardEl = document.getElementById('flashcardElement');

        if (frontText) frontText.textContent = card.front_prompt;
        if (backText) backText.textContent = card.back_solution;
        if (tracker) tracker.textContent = `Card ${this.currentCardIndex + 1} / ${this.activeDeck.cards.length}`;

        if (cardEl) cardEl.classList.remove('flipped');
        this.isFlipped = false;
    },

    flipCard() {
        const cardEl = document.getElementById('flashcardElement');
        if (!cardEl) return;
        this.isFlipped = !this.isFlipped;
        cardEl.classList.toggle('flipped', this.isFlipped);
    },

    nextCard() {
        if (!this.activeDeck) return;
        if (this.currentCardIndex < this.activeDeck.cards.length - 1) {
            this.currentCardIndex++;
            this.updateCardDisplay();
        }
    },

    prevCard() {
        if (!this.activeDeck) return;
        if (this.currentCardIndex > 0) {
            this.currentCardIndex--;
            this.updateCardDisplay();
        }
    }
};

window.FlashcardComponent = FlashcardComponent;
