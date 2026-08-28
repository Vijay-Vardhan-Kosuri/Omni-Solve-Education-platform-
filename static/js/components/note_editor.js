/**
 * Student Note Editor Component
 */
const NoteEditorComponent = {
    init() {
        AppState.subscribe(state => this.renderNotesList(state));

        const saveBtn = document.getElementById('saveNoteBtn');
        const newBtn = document.getElementById('newNoteBtn');

        if (saveBtn) saveBtn.addEventListener('click', () => this.saveNote());
        if (newBtn) newBtn.addEventListener('click', () => this.clearEditor());
    },

    renderNotesList(state) {
        const container = document.getElementById('notesListContainer');
        if (!container) return;

        if (state.studentNotes.length === 0) {
            container.innerHTML = '<p style="color:var(--text-muted); padding:0.5rem;">No saved notes.</p>';
            return;
        }

        container.innerHTML = state.studentNotes.map(n => `
            <div class="note-item" onclick="NoteEditorComponent.loadNote(${n.id})">
                <h4>${this.escapeHtml(n.title)}</h4>
                <p>${n.updated_at} • ${n.subject_code}</p>
            </div>
        `).join('');
    },

    loadNote(noteId) {
        const note = AppState.studentNotes.find(n => n.id === noteId);
        if (!note) return;

        document.getElementById('noteTitleInput').value = note.title;
        document.getElementById('noteContentTextarea').value = note.content_markdown;
    },

    clearEditor() {
        document.getElementById('noteTitleInput').value = '';
        document.getElementById('noteContentTextarea').value = '';
    },

    async saveNote() {
        const title = document.getElementById('noteTitleInput').value.trim();
        const content = document.getElementById('noteContentTextarea').value.trim();

        if (!title || !content) {
            alert('Please provide title and note content.');
            return;
        }

        const payload = {
            title: title,
            content_markdown: content,
            subject_code: AppState.activeSubjectFilter === 'ALL' ? 'MATH' : AppState.activeSubjectFilter
        };

        const res = await fetch('/api/flashcards/notes/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        const data = await res.json();
        if (data.status === 'success') {
            await AppState.fetchNotes();
            alert('Note saved successfully!');
        }
    },

    escapeHtml(str) {
        if (!str) return '';
        return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
    }
};

window.NoteEditorComponent = NoteEditorComponent;
