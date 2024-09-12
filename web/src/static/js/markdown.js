/*
File: markdown.js
Author: Chuncheng Zhang
Date: 2024-09-10
Copyright & Email: chuncheng.zhang@ia.ac.cn

Purpose:
    Read and render the markdown documents into the HTML document

Functions:
    1. Requirements and constants
    2. Function and class
    3. Play ground
    4. Pending
    5. Pending
*/

// %% ---- 2024-09-10 ------------------------
// Requirements and constants

// %% ---- 2024-09-10 ------------------------
// Function and class
function renderMarkdownIntoHTML(topic, path, dom) {
    d3.json(`/getContentMd?topic=${topic}&path=${path}`).then((json) => {
        let mdi = markdownit(
            {
                highlight: function (str, lang) {
                    if (lang && hljs.getLanguage(lang)) {
                        try {
                            return '<pre><code class="hljs">' +
                                hljs.highlight(str, { language: lang, ignoreIllegals: true }).value +
                                '</code></pre>';
                        } catch (err) { console.error(err) }
                    }

                    return '<pre><code class="hljs">' + mdi.utils.escapeHtml(str) + '</code></pre>';
                }
            }
        ),
            html = mdi.render(json.content);

        // Clear the current content
        dom.innerHTML = ''

        /* Insert the new content
            Author              Date
            Title
            -------------------------
            Others
        */
        let head = d3.select(dom).append('div'),
            hp = head.append('p').attr('class', 'flex justify-between gap-x-6 py-5'),
            dsd = d3.select(dom).append('div');

        // Insert the html of markdown
        dsd.node().innerHTML = html;

        // Append title
        head.append('h1').attr("class", "my-8 text-4xl font-bold").text(json.Title)

        // Append author and date
        hp.append('span').text(json.Author).attr("class", "text-sm italic leading-6 text-gray-900")
        hp.append('span').text(json.Date).attr("class", "mt-1 text-sm leading-5 text-gray-500")

        // Attach the class
        dsd.selectAll('p').attr('class', 'text-base py-2')
        dsd.selectAll("h1").attr("class", "my-8 text-4xl font-bold");
        dsd.selectAll('h2').attr("class", "my-4 text-2xl font-bold");
        dsd.selectAll('h3').attr("class", "my-4 text-xl font-bold");
        dsd.selectAll('a').attr('class', 'italic text-green-800')
        dsd.selectAll('ul').attr('class', 'px-6').selectAll('li').attr('class', 'list-disc text-base ')
        dsd.selectAll('ol').attr('class', 'px-6').selectAll('li').attr('class', 'list-decimal text-base ')
        dsd.selectAll('.hljs-comment').attr('class', 'hljs-comment italic')
        // dsd.selectAll('pre').attr('class', 'bg-sky-100')
    });
}

// %% ---- 2024-09-10 ------------------------
// Play ground

// %% ---- 2024-09-10 ------------------------
// Pending

// %% ---- 2024-09-10 ------------------------
// Pending
