document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('srs_short');
    const totalScoreDisplay = document.getElementById('totalScore');

    // 定義包含問題內容的陣列
    const questions = [
        '1. 被別的孩子認為是古怪或奇特的',
        '2. 在與同儕一來一往互動時是笨拙的(例如:似乎不瞭解對話所需的一來一往)',
        '3. 和同齡孩子適當地玩在一起',
        '4. 和其他孩子相比，要改變生活慣例更為困難',
        '5. 與同儕相處有困難',
        // 添加更多問題內容
    ];

    // 動態生成問題和選項
    questions.forEach(function(questionText, index) {
        const questionContainer = document.createElement('div');

        // 添加問題標題
        const questionTitle = document.createElement('p');
        questionTitle.textContent = questionText;
        questionContainer.appendChild(questionTitle);

        // 添加相同的選項
        const options = ['不符合', '有些符合', '經常符合', '幾乎總是符合'];
        options.forEach(function(option, optionIndex) {
            const label = document.createElement('label');
            const radio = document.createElement('input');
            radio.type = 'radio';
            radio.name = `question${index + 1}`;
            radio.value = optionIndex + 1;
            if (optionIndex === 0) {
                radio.required = true; // 第一個選項設為必填
            }
            label.appendChild(radio);
            label.appendChild(document.createTextNode(option));
            questionContainer.appendChild(label);
        });

        // 添加間隔
        questionContainer.appendChild(document.createElement('br'));
        questionContainer.appendChild(document.createElement('br'));

        // 將問題添加到表單中
        form.appendChild(questionContainer);
    });

    // 添加提交按鈕
    const submitButton = document.createElement('button');
    submitButton.type = 'submit';
    submitButton.textContent = '提交';
    form.appendChild(submitButton);

    // 提交表單時的邏輯
    form.addEventListener('submit', function(event) {
        event.preventDefault(); // 阻止表單默認提交行為

        // 計算總分
        let totalScore = 0;
        for (let i = 1; i <= questions.length; i++) {
            const selectedOption = document.querySelector(`input[name="question${i}"]:checked`);
            if (selectedOption) {
                totalScore += parseInt(selectedOption.value);
            }
        }

        // 顯示總分
        // const totalScoreDisplay = document.createElement('div');
        totalScoreDisplay.textContent = `您的總分為：${totalScore}`;
        // form.appendChild(totalScoreDisplay);

        // 判斷是否通過
        // const passMessage = document.createElement('div');
        if (totalScore > 10) {
            alert(totalScoreDisplay.textContent += ' 恭喜您，您已經通過關卡！');
        } else {
            alert(totalScoreDisplay.textContent += ' 很遺憾，您未能通過關卡。');
        }
        // form.appendChild(passMessage);

        window.location.href = 'index.html';

        //重置表單
        form.reset();
    });
});
