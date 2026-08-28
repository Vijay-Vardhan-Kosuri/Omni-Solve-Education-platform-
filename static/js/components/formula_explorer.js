/**
 * Interactive Formula Explorer Component
 */
const FormulaExplorerComponent = {
    init() {
        AppState.subscribe(() => this.render());
        this.render();
    },

    render() {
        const container = document.getElementById('formulaCardsGrid');
        if (!container) return;

        let allFormulas = [
            ...window.MathKnowledge.formulas.map(f => ({ ...f, subject: 'MATH', color: '#2563EB' })),
            ...window.PhysicsKnowledge.formulas.map(f => ({ ...f, subject: 'PHYS', color: '#EC4899' })),
            ...window.ChemistryKnowledge.formulas.map(f => ({ ...f, subject: 'CHEM', color: '#8B5CF6' })),
            ...window.CSKnowledge.formulas.map(f => ({ ...f, subject: 'CS', color: '#10B981' })),
            ...window.BiologyKnowledge.formulas.map(f => ({ ...f, subject: 'BIO', color: '#F59E0B' })),
            ...window.AptitudeKnowledge.formulas.map(f => ({ ...f, subject: 'APT', color: '#06B6D4' }))
        ];

        if (AppState.activeSubjectFilter !== 'ALL') {
            allFormulas = allFormulas.filter(f => f.subject === AppState.activeSubjectFilter);
        }

        if (AppState.searchQuery) {
            const q = AppState.searchQuery.toLowerCase();
            allFormulas = allFormulas.filter(f => f.name.toLowerCase().includes(q) || f.expression.toLowerCase().includes(q) || f.description.toLowerCase().includes(q));
        }

        container.innerHTML = allFormulas.map(f => `
            <div class="formula-card">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.5rem;">
                    <span class="subject-badge" style="background-color:${f.color};">${f.subject}</span>
                    <span style="font-size:0.75rem; color:var(--text-muted);">${f.category}</span>
                </div>
                <div class="formula-name">${f.name}</div>
                <div class="formula-expr">${f.expression}</div>
                <p style="font-size:0.85rem; color:var(--text-secondary); margin-bottom:0.6rem;">${f.description}</p>
                <div style="font-size:0.78rem; color:var(--text-muted);">
                    <strong>Variables:</strong> ${f.variables ? f.variables.join(', ') : 'N/A'}
                </div>
            </div>
        `).join('');
    }
};

window.FormulaExplorerComponent = FormulaExplorerComponent;
