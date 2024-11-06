## Static Site Generator (SSG)
### Objectives
* Build a SEO and performance optimized SSG (like a cheap version of Hugo) to convert markdown files into html files from scratch.
* Reinforce my knowledge of OOP and FP using python in a web project.

### Architecture
The flow of data through the full system is :
1. `.md` files are in the `/content` directory. A `template.html` file is in the root of the project.
2. The SSG in `src/` reads the `.md` files and the template file.
3. The SSG converts the markdown files to a final HTML file for each page and writes them to the `/public` directory.
4. With the Python HTTP server, we serve the contents of the `/public` directory on a localhost.
5. We can view the final content on the browser through the localhost.

### How the SSG works
The vast majority of the SSG is in the `src/` directory. Here's how it runs :
1. Delete everything in the `/public` directory.
2. Copy any static assets (templates, images, css etc.) to the `public` directory.
3. Generate an HTML file for each markdown file in the `/content`  directory:
	1. Open and read the file.
	2. Split the markdown into "blocks" (paragraphs, headings, lists etc.)
	3. Convert each block into a tree of `HTMLNode` objects. For inline elements (bold, links, italic etc.) we'll convert raw markdown syntax to `TextNode` and then to `HTMLNode`.
	4. Join the `HTMLNode` blocks under one large parent `HTMLNode` for the pages.
	5. Use a recursive `to_html()` method to convert the `HTMLNode` and all it's nested nodes to a giant HTML string and inject it in the HTML template.
	6. Write the full HTML string to a file for that page in the `/public` directory.
	
