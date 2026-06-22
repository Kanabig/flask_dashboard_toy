document.addEventListener('DOMContentLoaded', function() {
    const titleInput = document.getElementById('diaryTitleInput');
    const titleOutput = document.getElementById('noteTitleOutput');
    const contentInput = document.getElementById('diaryContentInput');
    const contentOutput = document.getElementById('noteContentOutput');

    titleInput.addEventListener('input', function() {
        titleOutput.innerText = this.value === "" ? "제목 없음" : this.value;
    });

    contentInput.addEventListener('input', function() {
        contentOutput.innerText = this.value === "" ? "여기에 내용이 표시됩니다." : this.value;
    });
}); 

function diaryform() {
    alert('저장완료!')
    document.diary_form.submit();
}
