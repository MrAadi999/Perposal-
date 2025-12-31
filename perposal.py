from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AADI ZONE - Special Proposal</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
            overflow: hidden;
        }

        .branding {
            position: absolute;
            top: 20px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 1.2rem;
            color: #ffd700;
            font-weight: bold;
            letter-spacing: 3px;
            text-shadow: 0 0 10px rgba(255, 215, 0, 0.5);
            padding: 10px 30px;
            border: 2px solid #ffd700;
            border-radius: 30px;
            background: rgba(255, 215, 0, 0.1);
        }

        .container {
            text-align: center;
            padding: 50px;
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            border-radius: 30px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 0 25px 50px rgba(0, 0, 0, 0.3);
            max-width: 500px;
            width: 90%;
        }

        h1 {
            color: #fff;
            font-size: 2.2rem;
            margin-bottom: 10px;
            text-shadow: 0 0 20px rgba(255, 105, 180, 0.5);
        }

        .subtitle {
            color: #ff69b4;
            font-size: 1.1rem;
            margin-bottom: 40px;
            font-style: italic;
        }

        .heart-icon {
            font-size: 4rem;
            margin-bottom: 20px;
            animation: pulse 1.5s ease-in-out infinite;
            display: inline-block;
        }

        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.1); }
        }

        .button-container {
            display: flex;
            justify-content: center;
            gap: 30px;
            margin: 40px 0;
            position: relative;
            min-height: 80px;
        }

        .btn {
            padding: 18px 50px;
            font-size: 1.3rem;
            font-weight: bold;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            transition: all 0.3s ease;
            text-transform: uppercase;
            letter-spacing: 2px;
            position: relative;
            overflow: hidden;
        }

        .btn::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
            transition: left 0.5s;
        }

        .btn:hover::before {
            left: 100%;
        }

        #yes-btn {
            background: linear-gradient(135deg, #00b894, #00cec9);
            color: white;
            box-shadow: 0 10px 30px rgba(0, 206, 201, 0.4);
        }

        #yes-btn:hover {
            transform: translateY(-3px) scale(1.05);
            box-shadow: 0 15px 40px rgba(0, 206, 201, 0.5);
        }

        #no-btn {
            background: linear-gradient(135deg, #e17055, #d63031);
            color: white;
            box-shadow: 0 10px 30px rgba(214, 48, 49, 0.4);
            position: relative;
        }

        #no-btn:hover {
            transform: translateY(-3px) scale(1.05);
            box-shadow: 0 15px 40px rgba(214, 48, 49, 0.5);
        }

        #msg {
            color: #ffd700;
            font-size: 1.8rem;
            margin-top: 30px;
            min-height: 60px;
            text-shadow: 0 0 20px rgba(255, 215, 0, 0.5);
            animation: fadeIn 0.5s ease;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .celebration {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 1000;
        }

        .confetti {
            position: absolute;
            width: 10px;
            height: 10px;
            background: #ffd700;
            animation: confetti-fall 3s ease-out forwards;
        }

        @keyframes confetti-fall {
            0% { transform: translateY(-100%) rotate(0deg); opacity: 1; }
            100% { transform: translateY(100vh) rotate(720deg); opacity: 0; }
        }

        .firework {
            position: absolute;
            width: 5px;
            height: 5px;
            border-radius: 50%;
            animation: firework 1s ease-out forwards;
        }

        @keyframes firework {
            0% { transform: scale(1); opacity: 1; }
            100% { transform: scale(3); opacity: 0; }
        }

        .floating-hearts {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            overflow: hidden;
            z-index: 999;
        }

        .floating-heart {
            position: absolute;
            font-size: 2rem;
            animation: float-up 4s ease-in forwards;
            opacity: 0;
        }

        @keyframes float-up {
            0% { transform: translateY(100vh) scale(0); opacity: 0; }
            10% { opacity: 1; }
            100% { transform: translateY(-100px) scale(1.5); opacity: 0; }
        }

        .glow-effect {
            position: absolute;
            width: 200px;
            height: 200px;
            background: radial-gradient(circle, rgba(255, 105, 180, 0.3) 0%, transparent 70%);
            border-radius: 50%;
            animation: glow 3s ease-in-out infinite;
            z-index: -1;
        }

        @keyframes glow {
            0%, 100% { transform: scale(1); opacity: 0.5; }
            50% { transform: scale(1.2); opacity: 1; }
        }
    </style>
</head>
<body>

    <div class="branding">✨ AADI ZONE ✨</div>

    <div class="glow-effect" style="top: 20%; left: 20%;"></div>
    <div class="glow-effect" style="top: 60%; right: 20%; animation-delay: 1s;"></div>

    <div class="floating-hearts" id="floating-hearts"></div>
    <div class="celebration" id="celebration"></div>

    <div class="container">
        <div class="heart-icon">💖</div>
        <h1>Will You Accept My Perposal?</h1>
        <p class="subtitle">A special question from my heart to yours 💕</p>

        <div class="button-container">
            <button id="yes-btn" class="btn" onclick="yes()">YES</button>
            <button id="no-btn" class="btn" onmouseover="move()" onclick="move()">NO</button>
        </div>

        <h2 id="msg"></h2>
    </div>

    <script>
        function yes() {
            document.getElementById("msg").innerHTML = 
                "❤️ Thank you for saying YES! ❤️<br><span style='font-size: 1rem; color: #fff;'>You just made me the happiest person! 💕</span>";
            
            document.getElementById("yes-btn").style.display = "none";
            document.getElementById("no-btn").style.display = "none";
            
            // Create celebration
            createCelebration();
            createFloatingHearts();
            
            // Change background to celebration mode
            document.body.style.background = "linear-gradient(135deg, #1a1a2e 0%, #2d132c 50%, #801336 100%)";
        }

        function move() {
            const btn = document.getElementById("no-btn");
            
            // Get actual button dimensions
            const btnRect = btn.getBoundingClientRect();
            const btnWidth = btnRect.width;
            const btnHeight = btnRect.height;
            
            // Safe area - keep within viewport with padding
            const padding = 20;
            const brandingHeight = 80; // Space for branding at top
            
            // Calculate boundaries
            const minX = padding;
            const minY = padding + brandingHeight;
            const maxX = window.innerWidth - btnWidth - padding;
            const maxY = window.innerHeight - btnHeight - padding;
            
            // Ensure we have valid bounds
            const safeMinX = Math.min(minX, maxX);
            const safeMinY = Math.min(minY, maxY);
            const safeMaxX = Math.max(minX, maxX);
            const safeMaxY = Math.max(minY, maxY);
            
            // Random position within safe bounds
            let x = Math.random() * (safeMaxX - safeMinX) + safeMinX;
            let y = Math.random() * (safeMaxY - safeMinY) + safeMinY;
            
            // Apply new position
            btn.style.position = 'fixed';
            btn.style.left = x + 'px';
            btn.style.top = y + 'px';
            btn.style.margin = '0';
        }

        function createCelebration() {
            const celebration = document.getElementById('celebration');
            
            // Create confetti
            for (let i = 0; i < 100; i++) {
                setTimeout(() => {
                    const confetti = document.createElement('div');
                    confetti.className = 'confetti';
                    confetti.style.left = Math.random() * 100 + '%';
                    confetti.style.background = ['#ffd700', '#ff69b4', '#00cec9', '#00b894', '#e17055'][Math.floor(Math.random() * 5)];
                    confetti.style.animationDuration = (Math.random() * 2 + 2) + 's';
                    confetti.style.width = (Math.random() * 10 + 5) + 'px';
                    confetti.style.height = confetti.style.width;
                    celebration.appendChild(confetti);
                    
                    setTimeout(() => confetti.remove(), 4000);
                }, i * 30);
            }

            // Create fireworks
            for (let i = 0; i < 50; i++) {
                setTimeout(() => {
                    const firework = document.createElement('div');
                    firework.className = 'firework';
                    firework.style.left = Math.random() * 100 + '%';
                    firework.style.top = Math.random() * 60 + '%';
                    firework.style.background = ['#ffd700', '#ff69b4', '#00cec9', '#fff'][Math.floor(Math.random() * 4)];
                    firework.style.boxShadow = `0 0 20px ${firework.style.background}`;
                    celebration.appendChild(firework);
                    
                    setTimeout(() => firework.remove(), 1000);
                }, i * 100);
            }
        }

        function createFloatingHearts() {
            const container = document.getElementById('floating-hearts');
            const hearts = ['💕', '💖', '💗', '💝', '❤️', '💘'];
            
            setInterval(() => {
                const heart = document.createElement('div');
                heart.className = 'floating-heart';
                heart.textContent = hearts[Math.floor(Math.random() * hearts.length)];
                heart.style.left = Math.random() * 100 + '%';
                heart.style.animationDuration = (Math.random() * 2 + 3) + 's';
                heart.style.fontSize = (Math.random() * 2 + 1.5) + 'rem';
                container.appendChild(heart);
                
                setTimeout(() => heart.remove(), 5000);
            }, 300);
        }
    </script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
    
