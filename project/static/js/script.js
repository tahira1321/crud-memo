// アラート表示
const Btn = document.getElementById('Btn');
if (Btn) {
    Btn.addEventListener('click', function() {
        alert('JavaScriptも動作中');
    });
}

// 次へ
const nextBtn = document.getElementById('nextBtn');
if (nextBtn) {
    nextBtn.addEventListener('click', function() {
        window.location.href = '/next';
    });
}

// 前へ
const prevBtn = document.getElementById('prevBtn');
if (prevBtn) {
    prevBtn.addEventListener('click', function() {
        window.history.back();
    });
}

