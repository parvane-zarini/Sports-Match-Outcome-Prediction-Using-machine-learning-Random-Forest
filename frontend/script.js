// بارگذاری لیست ورزش‌ها
window.onload = function() {
    fetch('http://127.0.0.1:5000/sports')
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                const sportSelect = document.getElementById('sport');
                data.sports.forEach(sport => {
                    const option = document.createElement('option');
                    option.value = sport;
                    option.textContent = sport;
                    sportSelect.appendChild(option);
                });
            } else {
                alert(data.message);
            }
        })
        .catch(error => {
            console.error('Error fetching sports:', error);
            alert('مشکلی در ارتباط با سرور وجود دارد.');
        });
};

// ارسال فرم برای پیش‌بینی
document.getElementById('predictionForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const sport = document.getElementById('sport').value;
    const score1 = document.getElementById('score1').value;
    const score2 = document.getElementById('score2').value;

    fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ sport, score1, score2 }),
    })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                document.getElementById('result').textContent = `برنده: ${data.winner}`;
            } else {
                alert(data.message);
            }
        })
        .catch(error => {
            console.error('Error making prediction:', error);
            alert('مشکلی در پیش‌بینی وجود دارد.');
        });
});
