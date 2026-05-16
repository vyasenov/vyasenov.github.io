-- Pandoc filter: count words in the document and inject a small "X min read" badge
-- at the top of the body. Used on blog posts via blog/_metadata.yml.

local WPM = 200

function Pandoc(doc)
    -- Skip listing pages (e.g. blog/index.qmd); reading time is only meaningful on posts.
    if doc.meta.listing ~= nil then return doc end

    local words = 0
    pandoc.walk_block(pandoc.Div(doc.blocks), {
        Str = function(s)
            if s.text:match("%w") then words = words + 1 end
        end
    })

    local minutes = math.max(1, math.ceil(words / WPM))
    local label = minutes .. " min read"
    local html = '<div class="reading-time">' .. label .. '</div>'
    table.insert(doc.blocks, 1, pandoc.RawBlock("html", html))
    return doc
end
