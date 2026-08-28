/**
 * OmniSolve EduClear - Reactive Application State & API Store
 */

const AppState = {
    activeTab: 'solver',
    activeSubjectFilter: 'ALL',
    activeDifficultyFilter: '',
    searchQuery: '',
    
    doubts: [],
    forumQuestions: [],
    flashcardDecks: [],
    studentNotes: [],
    whiteboards: [],

    listeners: [],

    subscribe(callback) {
        this.listeners.push(callback);
    },

    notify() {
        this.listeners.forEach(cb => cb(this));
    },

    async fetchDoubts() {
        try {
            let url = `/api/doubts/?subject=${this.activeSubjectFilter === 'ALL' ? '' : this.activeSubjectFilter}&q=${encodeURIComponent(this.searchQuery)}&difficulty=${this.activeDifficultyFilter}`;
            const res = await fetch(url);
            const data = await res.json();
            if (data.status === 'success') {
                this.doubts = data.doubts;
                this.notify();
            }
        } catch (e) {
            console.error('Error fetching doubts:', e);
        }
    },

    async fetchForumQuestions() {
        try {
            let url = `/api/forum/questions/?subject=${this.activeSubjectFilter === 'ALL' ? '' : this.activeSubjectFilter}&q=${encodeURIComponent(this.searchQuery)}`;
            const res = await fetch(url);
            const data = await res.json();
            if (data.status === 'success') {
                this.forumQuestions = data.questions;
                this.notify();
            }
        } catch (e) {
            console.error('Error fetching forum questions:', e);
        }
    },

    async fetchFlashcards() {
        try {
            let url = `/api/flashcards/decks/?subject=${this.activeSubjectFilter === 'ALL' ? '' : this.activeSubjectFilter}`;
            const res = await fetch(url);
            const data = await res.json();
            if (data.status === 'success') {
                this.flashcardDecks = data.decks;
                this.notify();
            }
        } catch (e) {
            console.error('Error fetching flashcards:', e);
        }
    },

    async fetchNotes() {
        try {
            let url = `/api/flashcards/notes/`;
            const res = await fetch(url);
            const data = await res.json();
            if (data.status === 'success') {
                this.studentNotes = data.notes;
                this.notify();
            }
        } catch (e) {
            console.error('Error fetching notes:', e);
        }
    },

    async submitDoubt(payload) {
        const res = await fetch('/api/doubts/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });
        const data = await res.json();
        if (data.status === 'success') {
            await this.fetchDoubts();
        }
        return data;
    },

    async upvoteDoubt(doubtId) {
        const res = await fetch(`/api/doubts/${doubtId}/upvote/`, { method: 'POST' });
        const data = await res.json();
        if (data.status === 'success') {
            const doubt = this.doubts.find(d => d.id === doubtId);
            if (doubt) doubt.upvotes = data.upvotes;
            this.notify();
        }
    }
};

window.AppState = AppState;
