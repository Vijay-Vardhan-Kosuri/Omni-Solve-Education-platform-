/**
 * OmniSolve EduClear - Application Bootstrapper & Router
 */

document.addEventListener('DOMContentLoaded', () => {
    // 1. Initialize Components
    DoubtSolverComponent.init();
    ForumComponent.init();
    WhiteboardComponent.init();
    FlashcardComponent.init();
    FormulaExplorerComponent.init();
    NoteEditorComponent.init();

    // 2. Initial Data Fetching
    AppState.fetchDoubts();
    AppState.fetchForumQuestions();
    AppState.fetchFlashcards();
    AppState.fetchNotes();

    // 3. Tab Switcher
    document.querySelectorAll('.nav-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
            document.querySelectorAll('.tab-content').forEach(tc => tc.classList.remove('active'));

            const target = e.currentTarget;
            target.classList.add('active');

            const tabId = target.dataset.tab;
            AppState.activeTab = tabId;

            const tabContent = document.getElementById(`tab-${tabId}`);
            if (tabContent) tabContent.classList.add('active');
        });
    });

    // 4. Subject Filter Pills
    document.querySelectorAll('.pill').forEach(pill => {
        pill.addEventListener('click', (e) => {
            document.querySelectorAll('.pill').forEach(p => p.classList.remove('active'));
            const target = e.currentTarget;
            target.classList.add('active');

            AppState.activeSubjectFilter = target.dataset.subject;
            AppState.fetchDoubts();
            AppState.fetchForumQuestions();
            AppState.fetchFlashcards();
            FormulaExplorerComponent.render();
        });
    });

    // 5. Global Search Input
    const searchInput = document.getElementById('globalSearchInput');
    if (searchInput) {
        searchInput.addEventListener('input', (e) => {
            AppState.searchQuery = e.target.value;
            AppState.fetchDoubts();
            AppState.fetchForumQuestions();
            FormulaExplorerComponent.render();
        });
    }

    // 6. Difficulty Filter Select
    const difficultySelect = document.getElementById('difficultyFilterSelect');
    if (difficultySelect) {
        difficultySelect.addEventListener('change', (e) => {
            AppState.activeDifficultyFilter = e.target.value;
            AppState.fetchDoubts();
        });
    }

    // 7. Theme Toggle
    const themeBtn = document.getElementById('themeToggleBtn');
    if (themeBtn) {
        themeBtn.addEventListener('click', () => {
            document.body.classList.toggle('light-theme');
            const isLight = document.body.classList.contains('light-theme');
            themeBtn.innerHTML = isLight ? '<i class="fa-solid fa-sun"></i>' : '<i class="fa-solid fa-moon"></i>';
        });
    }

    // 8. Modals Binding
    const askModal = document.getElementById('askDoubtModal');
    const askBtn = document.getElementById('askDoubtBtn');

    if (askBtn && askModal) {
        askBtn.addEventListener('click', () => askModal.classList.remove('hidden'));
    }

    document.querySelectorAll('[data-close]').forEach(btn => {
        btn.addEventListener('click', (e) => {
            const modalId = e.currentTarget.dataset.close;
            const modal = document.getElementById(modalId);
            if (modal) modal.classList.add('hidden');
        });
    });

    // 9. Submit Doubt Form
    const doubtForm = document.getElementById('askDoubtForm');
    if (doubtForm) {
        doubtForm.addEventListener('submit', async (e) => {
            e.preventDefault();

            const payload = {
                title: document.getElementById('doubtTitleInput').value.trim(),
                question_text: document.getElementById('doubtQuestionTextarea').value.trim(),
                subject_code: document.getElementById('doubtSubjectSelect').value,
                difficulty: document.getElementById('doubtDifficultySelect').value,
                latex_formula: document.getElementById('doubtLatexInput').value.trim(),
                code_snippet: document.getElementById('doubtCodeTextarea').value.trim(),
                student_name: 'Student'
            };

            const result = await AppState.submitDoubt(payload);
            if (result.status === 'success') {
                if (askModal) askModal.classList.add('hidden');
                doubtForm.reset();
                showToast('Doubt solved successfully with step-by-step steps!');
            }
        });
    }
});

function showToast(message) {
    const container = document.getElementById('toastContainer');
    if (!container) return;

    const toast = document.createElement('div');
    toast.className = 'toast';
    toast.innerHTML = `<i class="fa-solid fa-circle-check" style="color:var(--accent-green);"></i> ${message}`;

    container.appendChild(toast);
    setTimeout(() => {
        toast.remove();
    }, 4000);
}
