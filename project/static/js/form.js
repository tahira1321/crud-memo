// 1. documentを取得し定数に代入
const cancelBtn = document.getElementById('cancelBtn');
const memoForm = document.getElementById('memo-form');
if (cancelBtn) {
    cancelBtn.addEventListener('click', function() {
        if(confirm('本当にキャンセルしてもよろしいですか？')) {
            memoForm.reset()
        }
    });
}


