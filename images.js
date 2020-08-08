function danbooru(callback){
    const Danbooru = require('danbooru')
    const booru = new Danbooru()
    booru.posts({tags: 'rating:safe rem_(re:zero)'}).then(posts =>{
        const index = Math.floor(Math.random() * posts.length)
        const post = posts[index]
        const url = booru.url(post.file_url)
        const name = `${post.md5}.${post.file_ext}`
        exports.name = name
        require('https').get(url, response=>{
            var stream = response.pipe(require('fs').createWriteStream('./images/' + name))
            stream.on("end", callback);
        })
    }) 
}

exports.danbooru=danbooru

