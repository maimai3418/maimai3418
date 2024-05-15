document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('surveyForm');

    form.addEventListener('submit', function(event) {
        event.preventDefault(); // 阻止表單默認提交行為

        // 獲取用戶填寫的資料
        const name = document.getElementById('name').value;
        const birthday = new Date(document.getElementById('birthday').value);
        const fillDate = new Date();
        const gender = document.getElementById('gender').value;
        const feedback = document.getElementById('feedback').value;

        // 驗證用戶輸入
        if (name.trim() === '' || isNaN(birthday) || gender === '') {
            alert('請填寫完整的個人資訊！');
            return;
        }

        // 計算受試者年齡
        const ageDiffMs = fillDate - birthday;
        const ageDate = new Date(ageDiffMs);
        const ageYear = ageDate.getUTCFullYear() - 1970;
        const ageMonth = ageDate.getUTCMonth();

        // 處理用戶填寫的資料
        const userData = {
            name: name,
            birthday: birthday,
            fillDate: fillDate,
            age: ageYear,
            ageMonth: ageMonth,
            gender: gender,
            feedback: feedback
        };

        // 在實際應用中，你可以將userData發送到後端進行存儲或進一步處理
        console.log(userData);

        // 提示用戶提交成功並顯示年齡
        alert(`提交成功！您的年齡為：${ageYear}Y ${ageMonth}M`);
        window.location.href = 'srs_short.html';

        //重置表單
        form.reset();
    });
});