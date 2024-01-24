
document.addEventListener('DOMContentLoaded', function() {
    const images = document.querySelectorAll('.module-img');
    const modal = document.getElementById("myModal");
    const modalImg = document.getElementById("img01");
    const captionText = document.getElementById("caption");
    const close = document.getElementsByClassName("close")[0];

    images.forEach(img => {
        img.addEventListener('click', function() {
            modal.style.display = "block";
            modalImg.src = this.src;
            captionText.innerHTML = this.alt;
        });
    });

    close.onclick = function() { 
        modal.style.display = "none";
    };
});
