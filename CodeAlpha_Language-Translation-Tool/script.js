async function translateText() {

    const text = document.getElementById("inputText").value;
    const source = document.getElementById("sourceLang").value;
    const target = document.getElementById("targetLang").value;

    if (text.trim() === "") {
        alert("Please enter text");
        return;
    }

    document.getElementById("outputText").innerText = "Translating...";

    try {
        const response = await fetch(
            "https://api.mymemory.translated.net/get?q=" +
            encodeURIComponent(text) +
            "&langpair=" + source + "|" + target
        );

        const data = await response.json();

        let result = data.responseData.translatedText;

        // ✅ Fix wrong / same output
        if (!result || result.toLowerCase() === text.toLowerCase()) {
            document.getElementById("outputText").innerText =
                "⚠️ Translation not available. Try different text.";
            return;
        }

        document.getElementById("outputText").innerText = result;

    } catch (error) {
        document.getElementById("outputText").innerText =
            "⚠️ Error occurred";
    }
}
function swapLanguages() {
    let source = document.getElementById("sourceLang");
    let target = document.getElementById("targetLang");

    let temp = source.value;
    source.value = target.value;
    target.value = temp;
}
function clearText() {
    document.getElementById("inputText").value = "";
    document.getElementById("outputText").innerText = "";
    document.getElementById("charCount").innerText = "0 characters";
}
document.getElementById("inputText").addEventListener("input", function() {
    document.getElementById("charCount").innerText =
        this.value.length + " characters";
});


/* ✅ COPY BUTTON */
function copyText() {
    const text = document.getElementById("outputText").innerText;

    if (!text || text.includes("⚠️") || text === "Translating...") {
        alert("Nothing to copy!");
        return;
    }

    navigator.clipboard.writeText(text);
    alert("Copied!");
}


/* ✅ SPEAK BUTTON */
function speakText() {
    const text = document.getElementById("outputText").innerText.trim();
    const target = document.getElementById("targetLang").value;

    // 1. Check text
    if (!text || text === "" || text === "Translating..." || text.includes("⚠️")) {
        alert("Nothing to speak!");
        return;
    }

    // 2. Stop any previous speech
    window.speechSynthesis.cancel();

    // 3. Create utterance
    const utter = new SpeechSynthesisUtterance(text);

    // 4. Set language based on target
    utter.lang = (target === "hi") ? "hi-IN" : "en-US";

    // 5. Ensure voices are loaded (important fix)
    const setVoiceAndSpeak = () => {
        const voices = window.speechSynthesis.getVoices();

        // pick a matching voice if possible
        const voice = voices.find(v => v.lang === utter.lang) || voices[0];
        if (voice) utter.voice = voice;

        window.speechSynthesis.speak(utter);
    };

    // If voices not loaded yet, wait for them
    if (speechSynthesis.getVoices().length === 0) {
        speechSynthesis.onvoiceschanged = setVoiceAndSpeak;
    } else {
        setVoiceAndSpeak();
    }
}