/**
 * Interactive Scratchpad Whiteboard Component
 */
const WhiteboardComponent = {
    canvas: null,
    ctx: null,
    isDrawing: false,
    currentTool: 'pen',
    color: '#3B82F6',
    strokeWidth: 3,
    startX: 0,
    startY: 0,
    snapshot: null,

    init() {
        this.canvas = document.getElementById('whiteboardCanvas');
        if (!this.canvas) return;

        this.ctx = this.canvas.getContext('2d');
        this.bindEvents();
    },

    bindEvents() {
        // Tool selectors
        document.querySelectorAll('.wb-tool-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                document.querySelectorAll('.wb-tool-btn').forEach(b => b.classList.remove('active'));
                const target = e.currentTarget;
                target.classList.add('active');
                this.currentTool = target.dataset.tool;
            });
        });

        // Color & stroke
        const colorPicker = document.getElementById('wbColorPicker');
        if (colorPicker) {
            colorPicker.addEventListener('input', (e) => this.color = e.target.value);
        }

        const strokeSlider = document.getElementById('wbStrokeWidth');
        if (strokeSlider) {
            strokeSlider.addEventListener('input', (e) => this.strokeWidth = e.target.value);
        }

        // Clear canvas
        const clearBtn = document.getElementById('wbClearBtn');
        if (clearBtn) {
            clearBtn.addEventListener('click', () => {
                this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
            });
        }

        // Canvas mouse events
        this.canvas.addEventListener('mousedown', (e) => this.startDraw(e));
        this.canvas.addEventListener('mousemove', (e) => this.drawing(e));
        this.canvas.addEventListener('mouseup', () => this.stopDraw());
    },

    getPos(e) {
        const rect = this.canvas.getBoundingClientRect();
        return {
            x: e.clientX - rect.left,
            y: e.clientY - rect.top
        };
    },

    startDraw(e) {
        this.isDrawing = true;
        const pos = this.getPos(e);
        this.startX = pos.x;
        this.startY = pos.y;

        this.ctx.beginPath();
        this.ctx.lineWidth = this.strokeWidth;
        this.ctx.strokeStyle = this.currentTool === 'eraser' ? '#FFFFFF' : this.color;
        this.ctx.fillStyle = this.color;
        this.ctx.lineCap = 'round';

        this.snapshot = this.ctx.getImageData(0, 0, this.canvas.width, this.canvas.height);
    },

    drawing(e) {
        if (!this.isDrawing) return;
        const pos = this.getPos(e);

        if (this.currentTool === 'pen' || this.currentTool === 'eraser') {
            this.ctx.lineTo(pos.x, pos.y);
            this.ctx.stroke();
        } else {
            this.ctx.putImageData(this.snapshot, 0, 0);
            if (this.currentTool === 'line') {
                this.ctx.beginPath();
                this.ctx.moveTo(this.startX, this.startY);
                this.ctx.lineTo(pos.x, pos.y);
                this.ctx.stroke();
            } else if (this.currentTool === 'rect') {
                this.ctx.strokeRect(this.startX, this.startY, pos.x - this.startX, pos.y - this.startY);
            } else if (this.currentTool === 'circle') {
                const radius = Math.sqrt(Math.pow(pos.x - this.startX, 2) + Math.pow(pos.y - this.startY, 2));
                this.ctx.beginPath();
                this.ctx.arc(this.startX, this.startY, radius, 0, 2 * Math.PI);
                this.ctx.stroke();
            }
        }
    },

    stopDraw() {
        this.isDrawing = false;
    }
};

window.WhiteboardComponent = WhiteboardComponent;
