// ============================================================
//  1. THEME TOGGLE (works with both buttons)
// ============================================================
const body = document.body;
const toggleButtons = [
    document.getElementById('themeToggle1'),
    document.getElementById('themeToggle2')
];

// Load saved theme from localStorage
if (localStorage.getItem('theme') === 'dark') {
    body.classList.add('dark-theme');
}

// Update both buttons' icons based on current theme
function updateToggleIcons() {
    const isDark = body.classList.contains('dark-theme');
    toggleButtons.forEach(btn => {
        if (btn) {
            const icon = btn.querySelector('i');
            if (icon) {
                icon.className = isDark ? 'fa-solid fa-sun' : 'fa-solid fa-moon';
            }
        }
    });
}

// Initial icon update
updateToggleIcons();

// Add click event to both toggle buttons
toggleButtons.forEach(btn => {
    if (btn) {
        btn.addEventListener('click', function() {
            body.classList.toggle('dark-theme');
            const isDark = body.classList.contains('dark-theme');
            localStorage.setItem('theme', isDark ? 'dark' : 'light');
            updateToggleIcons();
        });
    }
});

// ============================================================
//  2. PREDICTION LOGIC (with real API)
// ============================================================
const predictBtn = document.getElementById('predictBtn');
const priceElement = document.getElementById('price');

predictBtn.addEventListener('click', predictPrice);

async function predictPrice() {

    // --- Collect data from inputs ---
    const data = {
        OverallQual: Number(document.getElementById('OverallQual').value),
        GrLivArea: Number(document.getElementById('GrLivArea').value),
        GarageCars: Number(document.getElementById('GarageCars').value),
        GarageArea: Number(document.getElementById('GarageArea').value),
        TotalBsmtSF: Number(document.getElementById('TotalBsmtSF').value),
        FullBath: Number(document.getElementById('FullBath').value),
        YearBuilt: Number(document.getElementById('YearBuilt').value),
        YearRemodAdd: Number(document.getElementById('YearRemodAdd').value),
        LotArea: Number(document.getElementById('LotArea').value),
        BedroomAbvGr: Number(document.getElementById('BedroomAbvGr').value)
    };

    // --- Validation: ensure all fields are filled and valid ---
    for (let key in data) {
        if (isNaN(data[key]) || data[key] === 0) {
            alert('⚠️ Please fill all fields with valid numbers (greater than 0).');
            return;
        }
    }

    // --- UI feedback: disable button, show loading ---
    predictBtn.disabled = true;
    predictBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Predicting...';

    try {
        // --- Send request to FastAPI backend ---
        const response = await fetch('http://127.0.0.1:8000/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            throw new Error(`Server responded with status ${response.status}`);
        }

        const result = await response.json();
        console.log('📊 Prediction result:', result);

        // --- Extract predicted price (handle different key names) ---
        const predictedPrice = Number(result.PredictedPrice || result.predicted_price || result.price);

        if (isNaN(predictedPrice) || predictedPrice <= 0) {
            throw new Error('Invalid price received from server.');
        }

        // --- Display formatted price in INR ---
        priceElement.innerHTML =
            '₹ ' +
            predictedPrice.toLocaleString('en-IN', {
                maximumFractionDigits: 2
            });

        // --- Animate price pop ---
        priceElement.style.transition = 'transform 0.2s ease';
        priceElement.style.transform = 'scale(1.2)';
        setTimeout(() => {
            priceElement.style.transform = 'scale(1)';
        }, 300);

    } catch (error) {
        console.error('❌ Error:', error);

        // --- Fallback: show a demo prediction if API fails ---
        const fallbackPrice = Math.floor(Math.random() * 8000000) + 2500000;
        priceElement.innerHTML =
            '₹ ' +
            fallbackPrice.toLocaleString('en-IN', {
                maximumFractionDigits: 2
            });

        // Show alert only if it's not a network error (optional)
        if (error.message.includes('Failed to fetch') || error.message.includes('Server')) {
            alert('⚠️ Unable to connect to FastAPI server.\nShowing demo prediction instead.');
        } else {
            alert('⚠️ ' + error.message);
        }

    } finally {
        // --- Restore button ---
        predictBtn.disabled = false;
        predictBtn.innerHTML = '<i class="fa-solid fa-wand-magic-sparkles"></i> Predict Price';
    }
}

// ============================================================
//  3. OPTIONAL: Auto-predict on page load (with demo values)
// ============================================================
// Pre-fill some demo values so the page looks alive
document.addEventListener('DOMContentLoaded', function() {
    // Set default example values
    document.getElementById('OverallQual').value = 7;
    document.getElementById('GrLivArea').value = 1800;
    document.getElementById('GarageCars').value = 2;
    document.getElementById('GarageArea').value = 500;
    document.getElementById('TotalBsmtSF').value = 900;
    document.getElementById('FullBath').value = 2;
    document.getElementById('YearBuilt').value = 2005;
    document.getElementById('YearRemodAdd').value = 2010;
    document.getElementById('LotArea').value = 8500;
    document.getElementById('BedroomAbvGr').value = 3;

    // Trigger prediction after a short delay
    setTimeout(() => {
        predictBtn.click();
    }, 500);
});