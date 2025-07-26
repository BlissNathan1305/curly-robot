<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>4K Portrait Mobile Wallpapers</title>
    <style>
        body {
            margin: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            background: #222;
            color: white;
            font-family: Arial, sans-serif;
            overflow-x: hidden;
        }
        canvas {
            display: block;
            width: 100%;
            max-width: 540px; /* Scale for mobile display */
            height: auto;
        }
        .controls {
            margin: 20px;
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            justify-content: center;
        }
        button {
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            background: #6200ea;
            color: white;
            border: none;
            border-radius: 5px;
        }
        button:hover {
            background: #3700b3;
        }
    </style>
</head>
<body>
    <canvas id="wallpaperCanvas"></canvas>
    <div class="controls">
        <button onclick="drawCosmicNebula()">Cosmic Nebula</button>
        <button onclick="drawFractalWaves()">Fractal Waves</button>
        <button onclick="drawCrystalMosaic()">Crystal Mosaic</button>
        <button onclick="downloadWallpaper()">Download Wallpaper</button>
    </div>
    <script>
        // Canvas setup
        const canvas = document.getElementById('wallpaperCanvas');
        const ctx = canvas.getContext('2d');
        const width = 2160; // Portrait 4K
        const height = 3840;
        canvas.width = width;
        canvas.height = height;
        canvas.style.maxWidth = `${Math.min(window.innerWidth, 540)}px`;
        canvas.style.height = 'auto';

        // Utility: Generate noise for texture
        function generateNoise(ctx, width, height, opacity = 0.04) {
            const imageData = ctx.createImageData(width, height);
            const data = imageData.data;
            for (let i = 0; i < data.length; i += 4) {
                const value = Math.random() * 255;
                data[i] = value;
                data[i + 1] = value;
                data[i + 2] = value;
                data[i + 3] = opacity * 255;
            }
            ctx.putImageData(imageData, 0, 0);
        }

        // Design 1: Cosmic Nebula
        function drawCosmicNebula() {
            ctx.fillStyle = '#000';
            ctx.fillRect(0, 0, width, height);

            // Vertical gradient for portrait
            const gradient = ctx.createLinearGradient(0, 0, 0, height);
            gradient.addColorStop(0, '#311b92');
            gradient.addColorStop(0.3, '#d81b60');
            gradient.addColorStop(0.6, '#0288d1');
            gradient.addColorStop(1, '#000');

            ctx.fillStyle = gradient;
            ctx.fillRect(0, 0, width, height);

            // Glowing stars
            ctx.globalCompositeOperation = 'lighter';
            for (let i = 0; i < 400; i++) { // Reduced for performance
                const x = Math.random() * width;
                const y = Math.random() * height;
                const radius = Math.random() * 2 + 0.5;
                const glow = ctx.createRadialGradient(x, y, 0, x, y, radius * 3);
                glow.addColorStop(0, 'rgba(255, 255, 255, 0.7)');
                glow.addColorStop(1, 'rgba(255, 255, 255, 0)');
                ctx.fillStyle = glow;
                ctx.beginPath();
                ctx.arc(x, y, radius * 3, 0, Math.PI * 2);
                ctx.fill();
            }

            generateNoise(ctx, width, height, 0.03);
            ctx.globalCompositeOperation = 'source-over';
        }

        // Design 2: Fractal Waves
        function drawFractalWaves() {
            ctx.fillStyle = '#0a192f';
            ctx.fillRect(0, 0, width, height);

            // Vertical gradient
            const gradient = ctx.createLinearGradient(0, 0, 0, height);
            gradient.addColorStop(0, '#64b5f6');
            gradient.addColorStop(0.5, '#ab47bc');
            gradient.addColorStop(1, '#ff7043');

            ctx.fillStyle = gradient;
            ctx.fillRect(0, 0, width, height);

            // Wave patterns
            ctx.globalCompositeOperation = 'screen';
            for (let y = 0; y < height; y += 10) { // Increased step for performance
                for (let x = 0; x < width; x += 10) {
                    const offsetX = Math.sin(y * 0.003 + x * 0.002) * 25;
                    const offsetY = Math.cos(x * 0.003 + y * 0.002) * 25;
                    ctx.fillStyle = `rgba(255, 255, 255, ${0.02 + Math.random() * 0.02})`;
                    ctx.beginPath();
                    ctx.arc(x + offsetX, y + offsetY, 4, 0, Math.PI * 2);
                    ctx.fill();
                }
            }

            generateNoise(ctx, width, height, 0.03);
            ctx.globalCompositeOperation = 'source-over';
        }

        // Design 3: Crystal Mosaic
        function drawCrystalMosaic() {
            ctx.fillStyle = '#1a237e';
            ctx.fillRect(0, 0, width, height);

            // Diagonal gradient
            const gradient = ctx.createLinearGradient(0, 0, width, height);
            gradient.addColorStop(0, '#4fc3f7');
            gradient.addColorStop(1, '#e91e63');

            ctx.fillStyle = gradient;
            ctx.fillRect(0, 0, width, height);

            // Elongated polygons for portrait
            ctx.globalCompositeOperation = 'overlay';
            const size = 120; // Adjusted for taller canvas
            for (let y = -size; y < height + size; y += size) {
                for (let x = -size; x < width + size; x += size) {
                    const offset = Math.random() * 20;
                    ctx.beginPath();
                    ctx.moveTo(x + offset, y);
                    ctx.lineTo(x + size / 2, y + size * 1.2); // Elongated
                    ctx.lineTo(x + size - offset, y);
                    ctx.lineTo(x + size * 0.7, y + size * 0.4);
                    ctx.closePath();
                    ctx.fillStyle = `rgba(255, 255, 255, ${0.1 + Math.random() * 0.1})`;
                    ctx.fill();
                    ctx.strokeStyle = 'rgba(255, 255, 255, 0.15)';
                    ctx.stroke();
                }
            }

            generateNoise(ctx, width, height, 0.03);
            ctx.globalCompositeOperation = 'source-over';
        }

        // Download function
        function downloadWallpaper() {
            const link = document.createElement('a');
            link.download = 'portrait-wallpaper.jpg';
            link.href = canvas.toDataURL('image/jpeg', 0.8); // 80% quality
            link.click();
        }

        // Draw default wallpaper
        drawCosmicNebula();
    </script>
</body>
</html>

