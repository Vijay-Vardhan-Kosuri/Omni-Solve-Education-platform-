/**
 * Doubt Solver UI Component
 */
const DoubtSolverComponent = {
    init() {
        AppState.subscribe(state => this.render(state));
    },

    render(state) {
        const container = document.getElementById('doubtsListContainer');
        const countSpan = document.getElementById('doubtsCount');
        if (!container) return;

        if (countSpan) countSpan.textContent = state.doubts.length;

        if (state.doubts.length === 0) {
            container.innerHTML = `
                <div class="empty-state" style="text-align:center; padding:3rem; color:var(--text-muted);">
                    <i class="fa-solid fa-folder-open" style="font-size:3rem; margin-bottom:1rem;"></i>
                    <p>No doubts found matching your search and filter criteria.</p>
                </div>
            `;
            return;
        }

        container.innerHTML = state.doubts.map(doubt => `
            <div class="doubt-card">
                <div class="card-header-bar">
                    <span class="subject-badge" style="background-color: ${doubt.subject_color || '#3B82F6'};">
                        ${doubt.subject_code}
                    </span>
                    <div class="card-meta">
                        <span><i class="fa-solid fa-user"></i> ${this.escapeHtml(doubt.student_name)}</span>
                        <span><i class="fa-solid fa-clock"></i> ${doubt.created_at}</span>
                        <span><i class="fa-solid fa-eye"></i> ${doubt.views_count} views</span>
                    </div>
                </div>

                <h3 class="doubt-card-title">${this.escapeHtml(doubt.title)}</h3>
                <p class="doubt-question-body">${this.escapeHtml(doubt.question_text)}</p>

                ${doubt.latex_formula ? `
                    <div class="latex-display-box">
                        <i class="fa-solid fa-square-root-variable"></i> ${this.escapeHtml(doubt.latex_formula)}
                    </div>
                ` : ''}

                ${doubt.code_snippet ? `
                    <div class="code-display-box">
                        <code>${this.escapeHtml(doubt.code_snippet)}</code>
                    </div>
                ` : ''}

                <div class="solution-section-title">
                    <i class="fa-solid fa-circle-check"></i> Step-by-Step Solution (${doubt.steps.length} Steps)
                </div>

                <div class="steps-timeline">
                    ${doubt.steps.map(step => `
                        <div class="step-item">
                            <div class="step-title-text">Step ${step.step_number}: ${this.escapeHtml(step.step_title)}</div>
                            <div class="step-explanation-text">${this.escapeHtml(step.explanation)}</div>
                            ${step.formula_used ? `
                                <div style="margin-top:0.4rem; font-family:var(--font-code); color:var(--accent-amber); font-size:0.85rem;">
                                    ${this.escapeHtml(step.formula_used)}
                                </div>
                            ` : ''}
                            ${step.code_output ? `
                                <div style="margin-top:0.4rem; font-family:var(--font-code); color:var(--accent-green); font-size:0.82rem; background:#090D16; padding:0.4rem; border-radius:4px;">
                                    ${this.escapeHtml(step.code_output)}
                                </div>
                            ` : ''}
                        </div>
                    `).join('')}
                </div>

                <div class="card-actions-bar">
                    <button class="upvote-btn" onclick="AppState.upvoteDoubt(${doubt.id})">
                        <i class="fa-solid fa-thumbs-up"></i> Helpful (${doubt.upvotes})
                    </button>
                    <span style="font-size:0.8rem; color:var(--text-muted);">Status: ${doubt.status}</span>
                </div>
            </div>
        `).join('');
    },

    escapeHtml(str) {
        if (!str) return '';
        return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
    }
};

window.DoubtSolverComponent = DoubtSolverComponent;
