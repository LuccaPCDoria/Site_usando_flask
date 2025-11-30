// ===============================
// Arquivo JS Principal do Projeto
// ===============================

// Log simples no console
console.log("main.js carregado com sucesso!");

// -------------------------------
// Animação suave nos cards
// -------------------------------
document.addEventListener("DOMContentLoaded", () => {
    const cards = document.querySelectorAll(".card");

    cards.forEach(card => {
        card.addEventListener("mouseover", () => {
            card.style.transform = "translateY(-4px)";
            card.style.transition = "0.2s";
            card.style.boxShadow = "0 4px 14px rgba(0,0,0,0.15)";
        });

        card.addEventListener("mouseout", () => {
            card.style.transform = "translateY(0)";
            card.style.boxShadow = "0 2px 8px rgba(0,0,0,0.07)";
        });
    });
});

// -------------------------------
// Suavizar scroll de âncoras
// -------------------------------
document.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener("click", function (e) {
        e.preventDefault();
        const alvo = document.querySelector(this.getAttribute("href"));
        if (alvo) {
            alvo.scrollIntoView({ behavior: "smooth", block: "start" });
        }
    });
});
