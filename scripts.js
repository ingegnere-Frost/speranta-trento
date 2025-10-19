function transposeChord(chord, semitones) {
    const scale_up = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"];
    const scale_down = ["c", "c#", "d", "d#", "e", "f", "f#", "g", "g#", "a", "a#", "b"];
    if (chord == chord.toUpperCase()) {
        const root = chord.match(/^[A-G][#b]?/)?.[0];
        if (!root) return chord;

        const suffix = chord.slice(root.length);
        const currentIndex = scale_up.indexOf(root);
        const newIndex = (currentIndex + semitones + 12) % 12;
        return scale_up[newIndex] + suffix;
    } else if (chord == chord.toLowerCase()) {
        const root = chord.match(/^[a-g][#b]?/)?.[0];
        if (!root) return chord;

        const suffix = chord.slice(root.length);
        const currentIndex = scale_down.indexOf(root);
        const newIndex = (currentIndex + semitones + 12) % 12;
        return scale_down[newIndex] + suffix;
    }
}

document.getElementById("transposeSelect").addEventListener("change", function () {
    const shift = parseInt(this.value);
    document.querySelectorAll("[data-chord]").forEach(el => {
    const originalChord = el.getAttribute("data-original") || el.getAttribute("data-chord");
    const transposedChord = transposeChord(originalChord, shift);
    el.setAttribute("data-chord", transposedChord);
    el.setAttribute("data-original", originalChord);
    });
});

document.getElementById("showChords").addEventListener("change", function () {
    document.querySelectorAll(".lyric").forEach(el => {
    el.classList.toggle("hide-chords", !this.checked);
    });
});