// scripts.js
document.addEventListener("DOMContentLoaded", () => {
    const artForm = document.getElementById('artForm');
    const commentForm = document.getElementById('commentForm');
    const artworksDiv = document.getElementById('artworks');
    const commentsList = document.getElementById('commentsList');

    artForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const title = e.target.title.value;
        const artist = e.target.artist.value;
        const image = e.target.image.value;

        const artDiv = document.createElement('div');
        artDiv.innerHTML = `<h3>${title}</h3><p>by ${artist}</p><img src="${image}" alt="${title}">`;
        artworksDiv.appendChild(artDiv);

        e.target.reset();
    });

    commentForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const commentText = e.target.comment.value;

        const commentDiv = document.createElement('div');
        commentDiv.textContent = commentText;
        commentsList.appendChild(commentDiv);

        e.target.reset();
    });
});
