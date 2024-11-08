document.addEventListener('DOMContentLoaded', () => {
    const linkContainers = document.querySelectorAll('.link-container');
    let index = 0;

    // Function to show links and descriptions two at a time
    const showNextLinks = () => {
        // Hide all links and descriptions
        linkContainers.forEach(container => {
            container.querySelector('a').style.display = 'none';
            container.querySelector('.description').style.display = 'none';
        });

        // Show the current two links and their descriptions
        for (let i = 0; i < 2; i++) {
            const currentContainer = linkContainers[index + i];
            if (currentContainer) { // Check if the currentContainer exists
                currentContainer.querySelector('a').style.display = 'block'; // Show the link
                currentContainer.querySelector('.description').style.display = 'block'; // Show the description
            }
        }

        index += 2; // Move to the next two links

        // Reset index if it exceeds the total number of links
        if (index >= linkContainers.length) {
            index = 0; // Reset to the first two links after showing all
        }

        setTimeout(showNextLinks, 60000); // Call the function again after 3 seconds
    };

    // Show only the first two links initially
    showNextLinks(); // Start the process
});