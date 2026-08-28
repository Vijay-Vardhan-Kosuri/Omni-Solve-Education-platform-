/**
 * Community Q&A Forum Component
 */
const ForumComponent = {
    init() {
        AppState.subscribe(state => this.render(state));
    },

    render(state) {
        const container = document.getElementById('forumQuestionsContainer');
        if (!container) return;

        if (state.forumQuestions.length === 0) {
            container.innerHTML = `
                <div style="text-align:center; padding:3rem; color:var(--text-muted);">
                    <i class="fa-solid fa-comments" style="font-size:3rem; margin-bottom:1rem;"></i>
                    <p>No community questions posted yet. Be the first to ask!</p>
                </div>
            `;
            return;
        }

        container.innerHTML = state.forumQuestions.map(q => `
            <div class="forum-card">
                <div class="forum-card-header">
                    <span class="forum-author"><i class="fa-solid fa-user-graduate"></i> ${this.escapeHtml(q.author_name)}</span>
                    <span style="font-size:0.8rem; color:var(--text-muted);">${q.created_at}</span>
                </div>
                <h3 class="forum-title">${this.escapeHtml(q.title)}</h3>
                <p class="forum-content">${this.escapeHtml(q.content)}</p>

                <div class="forum-tags">
                    ${q.tags.map(t => `<span class="tag-badge">#${this.escapeHtml(t)}</span>`).join('')}
                </div>

                <div class="answers-thread">
                    <div style="font-size:0.88rem; font-weight:700; color:var(--text-primary); margin-bottom:0.75rem;">
                        <i class="fa-solid fa-reply-all"></i> Answers (${q.answers.length})
                    </div>
                    ${q.answers.map(ans => `
                        <div class="answer-item">
                            <div class="answer-author">${this.escapeHtml(ans.author_name)} ${ans.is_accepted ? '<span style="color:var(--accent-green);">(Verified Solution)</span>' : ''}</div>
                            <div style="font-size:0.9rem; color:var(--text-secondary);">${this.escapeHtml(ans.content)}</div>
                        </div>
                    `).join('')}
                </div>
            </div>
        `).join('');
    },

    escapeHtml(str) {
        if (!str) return '';
        return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
    }
};

window.ForumComponent = ForumComponent;
