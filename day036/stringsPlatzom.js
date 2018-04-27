
function platzom(str){
    let translation = str

    str.toUpperCase()

    // If the word ends in "ar", that syllabe is removed
    if (str.toLowerCase().endsWith(`ar`)) {
        translation = str.slice(0, -2)
    }

    // If the word starts with Z, add "pe" at the beginning
    if (str.toLowerCase().startsWith(`z`)) {
        translation += `pe`
    }

    // If the translated word has 10 or more characters, a '-' should be added at the middle
    const length = translation.length

    if (length >= 10) {
        const firstHalf = translation.slice(0, Math.round(length / 2))
        const secondHalf = translation.slice(Math.round(length / 2))
        translation = `${firstHalf}-${secondHalf}`
    }

    // If original word is a palyndrome,
    // None of the rules is applied
    // Same word is written shifting uppercase and lowercase
    const reverse = (str) => str.split('').reverse().join('')

    function minMay(str) {
        const length = str.length
        let translation = ''
        let capitalize = true

        for (let i = 0; i < length; i++) {
            const char = str.charAt(i)
            translation += capitalize ? char.toUpperCase() : char.toLowerCase()
            capitalize = !capitalize
        }

        return translation

    }

    if (str == reverse(str)) {
        return minMay(str)
    }

    return translation
}

console.log(platzom("Almorzar"))
console.log(platzom("Zorro"))
console.log(platzom("abecedario"))
console.log(platzom("sometemos"))