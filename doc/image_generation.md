# 圖像生成

## 概覽

OpenAI API 讓你可以使用 GPT Image 模型，從文字提示生成與編輯圖片，包括我們最新的 `gpt-image-2`。你可以透過兩個 API 來使用圖片生成能力：

### Image API

從 `gpt-image-1` 與更新的模型開始，[Image API](https://developers.openai.com/api/docs/api-reference/images) 提供兩個端點，各自具備不同能力：

- **Generations**：根據文字提示從零開始[生成圖片](#generate-images)
- **Edits**：使用新的提示[修改現有圖片](#edit-images)，可部分或整體編輯

Image API 也包含一個 variations 端點，供支援此功能的模型使用，例如 DALL·E 2。

### Responses API

[Responses API](https://developers.openai.com/api/docs/api-reference/responses/create#responses-create-tools) 讓你能將圖片生成作為對話或多步驟流程的一部分。它支援圖片生成作為[內建工具](https://developers.openai.com/api/docs/guides/tools?api-mode=responses)，並可在上下文中接受圖片輸入與輸出。

與 Image API 相比，它新增了：

- **Multi-turn editing**：透過提示反覆進行高擬真度的圖片編輯
- **Flexible inputs**：接受圖片 [File](https://developers.openai.com/api/docs/api-reference/files) IDs 作為輸入圖片，而不僅限於 bytes

Responses API 的圖片生成工具使用其專屬的 GPT Image 模型選擇。關於支援呼叫此工具的主線模型詳情，請參考下方的[支援模型](#supported-models)。

### 選擇正確的 API

- 如果你只需要根據一個提示生成或編輯單一圖片，Image API 是你的最佳選擇。
- 如果你想使用 GPT Image 建立可對話、可編輯的圖片體驗，請選擇 Responses API。

這兩個 API 都能讓你透過調整品質、尺寸、格式與壓縮來[自訂輸出](#customize-image-output)。透明背景是否支援取決於模型支援情況。

本指南著重於 GPT Image。

為了確保這些模型被負責任地使用，你可能需要先完成 [API
  Organization
  Verification](https://help.openai.com/en/articles/10910291-api-organization-verification)
  ，可在你的 [developer
  console](https://platform.openai.com/settings/organization/general) 中進行，之後才能
  使用 GPT Image 模型，包括 `gpt-image-2`、`gpt-image-1.5`、
  `gpt-image-1` 與 `gpt-image-1-mini`。

<div
  className="not-prose"
  style={{ float: "right", margin: "10px 0 10px 10px" }}
>
  <img src="https://cdn.openai.com/API/docs/images/mug.png"
    alt="A beige coffee mug on a wooden table"
    style={{ height: "180px", width: "auto", borderRadius: "8px" }}
  />
</div>

## 生成圖片

你可以使用 [image generation endpoint](https://developers.openai.com/api/docs/api-reference/images/create) 依照文字提示建立圖片，或在 Responses API 中使用 [image generation tool](https://developers.openai.com/api/docs/guides/tools?api-mode=responses) 來在對話中生成圖片。

若要進一步瞭解如何自訂輸出內容（尺寸、品質、格式、壓縮），請參考下方的 [customize image output](#customize-image-output) 小節。

你可以將 `n` 參數設為一次生成多張圖片，透過單一請求完成（預設情況下，API 會回傳單張圖片）。



<div data-content-switcher-pane data-value="responses">
    <div class="hidden">Responses API</div>
    生成圖片

```javascript
import OpenAI from "openai";
const openai = new OpenAI();

const response = await openai.responses.create({
    model: "gpt-5.5",
    input: "Generate an image of gray tabby cat hugging an otter with an orange scarf",
    tools: [{type: "image_generation"}],
});

// Save the image to a file
const imageData = response.output
  .filter((output) => output.type === "image_generation_call")
  .map((output) => output.result);

if (imageData.length > 0) {
  const imageBase64 = imageData[0];
  const fs = await import("fs");
  fs.writeFileSync("otter.png", Buffer.from(imageBase64, "base64"));
}
```

```python
from openai import OpenAI
import base64

client = OpenAI() 

response = client.responses.create(
    model="gpt-5.5",
    input="Generate an image of gray tabby cat hugging an otter with an orange scarf",
    tools=[{"type": "image_generation"}],
)

# Save the image to a file
image_data = [
    output.result
    for output in response.output
    if output.type == "image_generation_call"
]
    
if image_data:
    image_base64 = image_data[0]
    with open("otter.png", "wb") as f:
        f.write(base64.b64decode(image_base64))
```

  </div>
  <div data-content-switcher-pane data-value="image" hidden>
    <div class="hidden">Image API</div>
    生成圖片

```javascript
import OpenAI from "openai";
import fs from "fs";
const openai = new OpenAI();

const prompt = \`
A children's book drawing of a veterinarian using a stethoscope to 
listen to the heartbeat of a baby otter.
\`;

const result = await openai.images.generate({
    model: "gpt-image-2",
    prompt,
});

// Save the image to a file
const image_base64 = result.data[0].b64_json;
const image_bytes = Buffer.from(image_base64, "base64");
fs.writeFileSync("otter.png", image_bytes);
```

```python
from openai import OpenAI
import base64
client = OpenAI()

prompt = """
A children's book drawing of a veterinarian using a stethoscope to 
listen to the heartbeat of a baby otter.
"""

result = client.images.generate(
    model="gpt-image-2",
    prompt=prompt
)

image_base64 = result.data[0].b64_json
image_bytes = base64.b64decode(image_base64)

# Save the image to a file
with open("otter.png", "wb") as f:
    f.write(image_bytes)
```

```bash
curl -X POST "https://api.openai.com/v1/images/generations" \\
    -H "Authorization: Bearer $OPENAI_API_KEY" \\
    -H "Content-type: application/json" \\
    -d '{
        "model": "gpt-image-2",
        "prompt": "A childrens book drawing of a veterinarian using a stethoscope to listen to the heartbeat of a baby otter."
    }' | jq -r '.data[0].b64_json' | base64 --decode > otter.png
```

```cli
openai images generate \\
  --model gpt-image-2 \\
  --prompt "A childrens book drawing of a veterinarian using a stethoscope to listen to the heartbeat of a baby otter." \\
  --raw-output \\
  --transform 'data.0.b64_json' | base64 --decode > otter.png
```

  </div>



### 多輪圖片生成

使用 Responses API 時，你可以透過在上下文中提供 image generation call 的輸出內容（你也可以直接使用 image ID），或使用 [`previous_response_id` 參數](https://developers.openai.com/api/docs/guides/conversation-state?api-mode=responses#openai-apis-for-conversation-state) 來建立包含圖片生成的多輪對話。
這讓你可以在多個回合中反覆調整圖片——精煉提示、套用新指示，並隨著對話進行逐步演進視覺輸出。

使用 Responses API 的 image generation tool 時，支援的 tool 模型可以自行決定是要生成新圖片，還是編輯對話中已經存在的圖片。可選的 `action` 參數可控制這個行為：保留 `action: "auto"` 讓模型自行決定，設定 `action: "generate"` 一律建立新圖片，或在上下文中已有圖片時設定 `action: "edit"` 強制進行編輯。

使用 action 強制建立圖片

```javascript
import OpenAI from "openai";
const openai = new OpenAI();

const response = await openai.responses.create({
    model: "gpt-5.5",
    input: "Generate an image of gray tabby cat hugging an otter with an orange scarf",
    tools: [{type: "image_generation", action: "generate"}],
});

// Save the image to a file
const imageData = response.output
  .filter((output) => output.type === "image_generation_call")
  .map((output) => output.result);

if (imageData.length > 0) {
  const imageBase64 = imageData[0];
  const fs = await import("fs");
  fs.writeFileSync("otter.png", Buffer.from(imageBase64, "base64"));
}
```

```python
from openai import OpenAI
import base64

client = OpenAI() 

response = client.responses.create(
    model="gpt-5.5",
    input="Generate an image of gray tabby cat hugging an otter with an orange scarf",
    tools=[{"type": "image_generation", "action": "generate"}],
)

# Save the image to a file
image_data = [
    output.result
    for output in response.output
    if output.type == "image_generation_call"
]
    
if image_data:
    image_base64 = image_data[0]
    with open("otter.png", "wb") as f:
        f.write(base64.b64decode(image_base64))
```


如果你強制使用 `edit` 但沒有在上下文中提供圖片，呼叫將會回傳錯誤。將 `action` 保持為 `auto`，讓模型決定何時生成或編輯。



<div data-content-switcher-pane data-value="responseid">
    <div class="hidden">Using previous response ID</div>
    多輪圖片生成

```javascript
import OpenAI from "openai";
const openai = new OpenAI();

const response = await openai.responses.create({
  model: "gpt-5.5",
  input:
    "Generate an image of gray tabby cat hugging an otter with an orange scarf",
  tools: [{ type: "image_generation" }],
});

const imageData = response.output
  .filter((output) => output.type === "image_generation_call")
  .map((output) => output.result);

if (imageData.length > 0) {
  const imageBase64 = imageData[0];
  const fs = await import("fs");
  fs.writeFileSync("cat_and_otter.png", Buffer.from(imageBase64, "base64"));
}

// Follow up

const response_fwup = await openai.responses.create({
  model: "gpt-5.5",
  previous_response_id: response.id,
  input: "Now make it look realistic",
  tools: [{ type: "image_generation" }],
});

const imageData_fwup = response_fwup.output
  .filter((output) => output.type === "image_generation_call")
  .map((output) => output.result);

if (imageData_fwup.length > 0) {
  const imageBase64 = imageData_fwup[0];
  const fs = await import("fs");
  fs.writeFileSync(
    "cat_and_otter_realistic.png",
    Buffer.from(imageBase64, "base64")
  );
}
```

```python
from openai import OpenAI
import base64

client = OpenAI()

response = client.responses.create(
    model="gpt-5.5",
    input="Generate an image of gray tabby cat hugging an otter with an orange scarf",
    tools=[{"type": "image_generation"}],
)

image_data = [
    output.result
    for output in response.output
    if output.type == "image_generation_call"
]

if image_data:
    image_base64 = image_data[0]

    with open("cat_and_otter.png", "wb") as f:
        f.write(base64.b64decode(image_base64))


# Follow up

response_fwup = client.responses.create(
    model="gpt-5.5",
    previous_response_id=response.id,
    input="Now make it look realistic",
    tools=[{"type": "image_generation"}],
)

image_data_fwup = [
    output.result
    for output in response_fwup.output
    if output.type == "image_generation_call"
]

if image_data_fwup:
    image_base64 = image_data_fwup[0]
    with open("cat_and_otter_realistic.png", "wb") as f:
        f.write(base64.b64decode(image_base64))
```

  </div>
  <div data-content-switcher-pane data-value="imageid" hidden>
    <div class="hidden">Using image ID</div>
    多輪圖片生成

```javascript
import OpenAI from "openai";
const openai = new OpenAI();

const response = await openai.responses.create({
  model: "gpt-5.5",
  input:
    "Generate an image of gray tabby cat hugging an otter with an orange scarf",
  tools: [{ type: "image_generation" }],
});

const imageGenerationCalls = response.output.filter(
  (output) => output.type === "image_generation_call"
);

const imageData = imageGenerationCalls.map((output) => output.result);

if (imageData.length > 0) {
  const imageBase64 = imageData[0];
  const fs = await import("fs");
  fs.writeFileSync("cat_and_otter.png", Buffer.from(imageBase64, "base64"));
}

// Follow up

const response_fwup = await openai.responses.create({
  model: "gpt-5.5",
  input: [
    {
      role: "user",
      content: [{ type: "input_text", text: "Now make it look realistic" }],
    },
    {
      type: "image_generation_call",
      id: imageGenerationCalls[0].id,
    },
  ],
  tools: [{ type: "image_generation" }],
});

const imageData_fwup = response_fwup.output
  .filter((output) => output.type === "image_generation_call")
  .map((output) => output.result);

if (imageData_fwup.length > 0) {
  const imageBase64 = imageData_fwup[0];
  const fs = await import("fs");
  fs.writeFileSync(
    "cat_and_otter_realistic.png",
    Buffer.from(imageBase64, "base64")
  );
}
```

```python
import openai
import base64

response = openai.responses.create(
    model="gpt-5.5",
    input="Generate an image of gray tabby cat hugging an otter with an orange scarf",
    tools=[{"type": "image_generation"}],
)

image_generation_calls = [
    output
    for output in response.output
    if output.type == "image_generation_call"
]

image_data = [output.result for output in image_generation_calls]

if image_data:
    image_base64 = image_data[0]

    with open("cat_and_otter.png", "wb") as f:
        f.write(base64.b64decode(image_base64))


# Follow up

response_fwup = openai.responses.create(
    model="gpt-5.5",
    input=[
        {
            "role": "user",
            "content": [{"type": "input_text", "text": "Now make it look realistic"}],
        },
        {
            "type": "image_generation_call",
            "id": image_generation_calls[0].id,
        },
    ],
    tools=[{"type": "image_generation"}],
)

image_data_fwup = [
    output.result
    for output in response_fwup.output
    if output.type == "image_generation_call"
]

if image_data_fwup:
    image_base64 = image_data_fwup[0]
    with open("cat_and_otter_realistic.png", "wb") as f:
        f.write(base64.b64decode(image_base64))
```

  </div>



#### 結果

<div className="not-prose">
  <table style={{ width: "100%" }}>
    <tbody>
      <tr>
        <td style={{ verticalAlign: "top", padding: "0 16px 16px 0" }}>
          "Generate an image of gray tabby cat hugging an otter with an orange
          scarf"
        </td>
        <td
          style={{
            textAlign: "right",
            verticalAlign: "top",
            paddingBottom: "16px",
          }}
        >
          <img src="https://cdn.openai.com/API/docs/images/cat_and_otter.png"
            alt="A cat and an otter"
            style={{ width: "200px", borderRadius: "8px" }}
          />
        </td>
      </tr>
      <tr>
        <td style={{ verticalAlign: "top", padding: "0 16px 0 0" }}>
          "Now make it look realistic"
        </td>
        <td style={{ textAlign: "right", verticalAlign: "top" }}>
          <img src="https://cdn.openai.com/API/docs/images/cat_and_otter_realistic.png"
            alt="A cat and an otter"
            style={{ width: "200px", borderRadius: "8px" }}
          />
        </td>
      </tr>
    </tbody>
  </table>
</div>

### 串流

Responses API 和 Image API 都支援圖片生成串流。你可以在 API 生成圖片時串流接收部分影像，提供更具互動性的體驗。

你可以調整 `partial_images` 參數來接收 0 到 3 張部分影像。

- 如果你將 `partial_images` 設為 0，你只會收到最終影像。
- 若值大於 0，當完整圖片生成得更快時，你可能不會收到你要求的全部部分影像。



<div data-content-switcher-pane data-value="responses">
    <div class="hidden">Responses API</div>
    串流圖片

```javascript
import OpenAI from "openai";
import fs from "fs";
const openai = new OpenAI();

const stream = await openai.responses.create({
  model: "gpt-5.5",
  input:
    "Draw a gorgeous image of a river made of white owl feathers, snaking its way through a serene winter landscape",
  stream: true,
  tools: [{ type: "image_generation", partial_images: 2 }],
});

for await (const event of stream) {
  if (event.type === "response.image_generation_call.partial_image") {
    const idx = event.partial_image_index;
    const imageBase64 = event.partial_image_b64;
    const imageBuffer = Buffer.from(imageBase64, "base64");
    fs.writeFileSync(\`river\${idx}.png\`, imageBuffer);
  }
}
```

```python
from openai import OpenAI
import base64

client = OpenAI()

stream = client.responses.create(
    model="gpt-5.5",
    input="Draw a gorgeous image of a river made of white owl feathers, snaking its way through a serene winter landscape",
    stream=True,
    tools=[{"type": "image_generation", "partial_images": 2}],
)

for event in stream:
    if event.type == "response.image_generation_call.partial_image":
        idx = event.partial_image_index
        image_base64 = event.partial_image_b64
        image_bytes = base64.b64decode(image_base64)
        with open(f"river{idx}.png", "wb") as f:
            f.write(image_bytes)
```

  </div>
  <div data-content-switcher-pane data-value="image" hidden>
    <div class="hidden">Image API</div>
    串流圖片

```javascript
import fs from "fs";
import OpenAI from "openai";

const openai = new OpenAI();

const prompt =
  "Draw a gorgeous image of a river made of white owl feathers, snaking its way through a serene winter landscape";
const stream = await openai.images.generate({
  prompt: prompt,
  model: "gpt-image-2",
  stream: true,
  partial_images: 2,
});

for await (const event of stream) {
  if (event.type === "image_generation.partial_image") {
    const idx = event.partial_image_index;
    const imageBase64 = event.b64_json;
    const imageBuffer = Buffer.from(imageBase64, "base64");
    fs.writeFileSync(\`river\${idx}.png\`, imageBuffer);
  }
}
```

```python
from openai import OpenAI
import base64

client = OpenAI()

stream = client.images.generate(
    prompt="Draw a gorgeous image of a river made of white owl feathers, snaking its way through a serene winter landscape",
    model="gpt-image-2",
    stream=True,
    partial_images=2,
)

for event in stream:
    if event.type == "image_generation.partial_image":
        idx = event.partial_image_index
        image_base64 = event.b64_json
        image_bytes = base64.b64decode(image_base64)
        with open(f"river{idx}.png", "wb") as f:
            f.write(image_bytes)
```

  </div>



#### 結果

<div className="images-examples">

| Partial 1                                                                                                                       | Partial 2                                                                                                                       | Final image                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| <img className="images-example-image" src="https://cdn.openai.com/API/docs/images/imgen1p5-streaming1.png" alt="1st partial" /> | <img className="images-example-image" src="https://cdn.openai.com/API/docs/images/imgen1p5-streaming2.png" alt="2nd partial" /> | <img className="images-example-image" src="https://cdn.openai.com/API/docs/images/imgen1p5-streaming3.png" alt="3rd partial" /> |

</div>

<div className="images-edit-prompt body-small">
  提示詞：Draw a gorgeous image of a river made of white owl feathers, snaking
  its way through a serene winter landscape
</div>

### 修訂提示詞

在 Responses API 中使用 image generation tool 時，主線模型（例如 `gpt-5.5`）會自動修訂你的提示詞，以提升表現。

你可以在 image generation call 的 `revised_prompt` 欄位中取得修訂後的提示詞：

修訂後的提示詞回應

```json
{
  "id": "ig_123",
  "type": "image_generation_call",
  "status": "completed",
  "revised_prompt": "A gray tabby cat hugging an otter. The otter is wearing an orange scarf. Both animals are cute and friendly, depicted in a warm, heartwarming style.",
  "result": "..."
}
```

## 編輯圖片

[圖片編輯](https://developers.openai.com/api/docs/api-reference/images/createEdit) 端點可讓你：

- 編輯既有圖片
- 使用其他圖片作為參考來生成新圖片
- 透過上傳圖片與標示要替換區域的遮罩來編輯圖片的部分內容

### 使用圖片參考建立新圖片

你可以使用一張或多張圖片作為參考來生成新圖片。

在這個範例中，我們會使用 4 張輸入圖片來生成一張包含參考圖片中物品的禮籃圖片。

<div data-content-switcher-pane data-value="responses">
    <div class="hidden">Responses API</div>
    </div>
  <div data-content-switcher-pane data-value="image" hidden>
    <div class="hidden">Image API</div>
    編輯圖片

```python
import base64
from openai import OpenAI
client = OpenAI()

prompt = """
Generate a photorealistic image of a gift basket on a white background 
labeled 'Relax & Unwind' with a ribbon and handwriting-like font, 
containing all the items in the reference pictures.
"""

result = client.images.edit(
    model="gpt-image-2",
    image=[
        open("body-lotion.png", "rb"),
        open("bath-bomb.png", "rb"),
        open("incense-kit.png", "rb"),
        open("soap.png", "rb"),
    ],
    prompt=prompt
)

image_base64 = result.data[0].b64_json
image_bytes = base64.b64decode(image_base64)

# Save the image to a file
with open("gift-basket.png", "wb") as f:
    f.write(image_bytes)
```

```javascript
import fs from "fs";
import OpenAI, { toFile } from "openai";

const client = new OpenAI();

const prompt = \`
Generate a photorealistic image of a gift basket on a white background 
labeled 'Relax & Unwind' with a ribbon and handwriting-like font, 
containing all the items in the reference pictures.
\`;

const imageFiles = [
    "bath-bomb.png",
    "body-lotion.png",
    "incense-kit.png",
    "soap.png",
];

const images = await Promise.all(
    imageFiles.map(async (file) =>
        await toFile(fs.createReadStream(file), null, {
            type: "image/png",
        })
    ),
);

const response = await client.images.edit({
    model: "gpt-image-2",
    image: images,
    prompt,
});

// Save the image to a file
const image_base64 = response.data[0].b64_json;
const image_bytes = Buffer.from(image_base64, "base64");
fs.writeFileSync("basket.png", image_bytes);
```

```bash
curl -s -D >(grep -i x-request-id >&2) \\
  -o >(jq -r '.data[0].b64_json' | base64 --decode > gift-basket.png) \\
  -X POST "https://api.openai.com/v1/images/edits" \\
  -H "Authorization: Bearer $OPENAI_API_KEY" \\
  -F "model=gpt-image-2" \\
  -F "image[]=@body-lotion.png" \\
  -F "image[]=@bath-bomb.png" \\
  -F "image[]=@incense-kit.png" \\
  -F "image[]=@soap.png" \\
  -F 'prompt=Generate a photorealistic image of a gift basket on a white background labeled "Relax & Unwind" with a ribbon and handwriting-like font, containing all the items in the reference pictures'
```

```cli
openai images edit \\
  --model gpt-image-2 \\
  --image body-lotion.png \\
  --image bath-bomb.png \\
  --image incense-kit.png \\
  --image soap.png \\
  --prompt 'Generate a photorealistic image of a gift basket on a white background labeled "Relax & Unwind" with a ribbon and handwriting-like font, containing all the items in the reference pictures' \\
  --raw-output \\
  --transform 'data.0.b64_json' | base64 --decode > gift-basket.png
```

  </div>



### 使用遮罩編輯圖片

你可以提供遮罩來指出應該編輯圖片的哪個部分。

當使用 GPT Image 搭配遮罩時，系統會另外傳送指示給模型，以協助其相應地引導編輯流程。

GPT Image 的遮罩完全是以提示詞為基礎。模型會使用遮罩作為
  引導，但不一定會完整精準地遵循其確切形狀。

如果你提供多張輸入圖片，遮罩會套用到第一張圖片上。



<div data-content-switcher-pane data-value="responses">
    <div class="hidden">Responses API</div>
    編輯帶有遮罩的圖片

```python
from openai import OpenAI
client = OpenAI()

fileId = create_file("sunlit_lounge.png")
maskId = create_file("mask.png")

response = client.responses.create(
    model="gpt-5.5",
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": "generate an image of the same sunlit indoor lounge area with a pool but the pool should contain a flamingo",
                },
                {
                    "type": "input_image",
                    "file_id": fileId,
                }
            ],
        },
    ],
    tools=[
        {
            "type": "image_generation",
            "quality": "high",
            "input_image_mask": {
                "file_id": maskId,
            }
        },
    ],
)

image_data = [
    output.result
    for output in response.output
    if output.type == "image_generation_call"
]

if image_data:
    image_base64 = image_data[0]
    with open("lounge.png", "wb") as f:
        f.write(base64.b64decode(image_base64))
```

```javascript
import OpenAI from "openai";
const openai = new OpenAI();

const fileId = await createFile("sunlit_lounge.png");
const maskId = await createFile("mask.png");

const response = await openai.responses.create({
  model: "gpt-5.5",
  input: [
    {
      role: "user",
      content: [
        {
          type: "input_text",
          text: "generate an image of the same sunlit indoor lounge area with a pool but the pool should contain a flamingo",
        },
        {
          type: "input_image",
          file_id: fileId,
        }
      ],
    },
  ],
  tools: [
    {
      type: "image_generation",
      quality: "high",
      input_image_mask: {
        file_id: maskId,
      }
    },
  ],
});

const imageData = response.output
  .filter((output) => output.type === "image_generation_call")
  .map((output) => output.result);

if (imageData.length > 0) {
  const imageBase64 = imageData[0];
  const fs = await import("fs");
  fs.writeFileSync("lounge.png", Buffer.from(imageBase64, "base64"));
}
```

  </div>
  <div data-content-switcher-pane data-value="image" hidden>
    <div class="hidden">Image API</div>
    編輯帶有遮罩的圖片

```python
from openai import OpenAI
client = OpenAI()

result = client.images.edit(
    model="gpt-image-2",
    image=open("sunlit_lounge.png", "rb"),
    mask=open("mask.png", "rb"),
    prompt="A sunlit indoor lounge area with a pool containing a flamingo"
)

image_base64 = result.data[0].b64_json
image_bytes = base64.b64decode(image_base64)

# Save the image to a file
with open("composition.png", "wb") as f:
    f.write(image_bytes)
```

```javascript
import fs from "fs";
import OpenAI, { toFile } from "openai";

const client = new OpenAI();

const rsp = await client.images.edit({
    model: "gpt-image-2",
    image: await toFile(fs.createReadStream("sunlit_lounge.png"), null, {
        type: "image/png",
    }),
    mask: await toFile(fs.createReadStream("mask.png"), null, {
        type: "image/png",
    }),
    prompt: "A sunlit indoor lounge area with a pool containing a flamingo",
});

// Save the image to a file
const image_base64 = rsp.data[0].b64_json;
const image_bytes = Buffer.from(image_base64, "base64");
fs.writeFileSync("lounge.png", image_bytes);
```

```bash
curl -s -D >(grep -i x-request-id >&2) \\
  -o >(jq -r '.data[0].b64_json' | base64 --decode > lounge.png) \\
  -X POST "https://api.openai.com/v1/images/edits" \\
  -H "Authorization: Bearer $OPENAI_API_KEY" \\
  -F "model=gpt-image-2" \\
  -F "mask=@mask.png" \\
  -F "image[]=@sunlit_lounge.png" \\
  -F 'prompt=A sunlit indoor lounge area with a pool containing a flamingo'
```

```cli
openai images edit \\
  --model gpt-image-2 \\
  --image sunlit_lounge.png \\
  --mask mask.png \\
  --prompt "A sunlit indoor lounge area with a pool containing a flamingo" \\
  --raw-output \\
  --transform 'data.0.b64_json' | base64 --decode > out.png
```

  </div>



<div className="images-examples">

| 圖片                                                                                                                                 | 遮罩                                                                                                                            | 輸出                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <img className="images-example-image" src="https://cdn.openai.com/API/docs/images/sunlit_lounge.png" alt="A pink room with a pool" /> | <img className="images-example-image" src="https://cdn.openai.com/API/docs/images/mask.png" alt="A mask in part of the pool" /> | <img className="images-example-image" src="https://cdn.openai.com/API/docs/images/sunlit_lounge_result.png" alt="The original pool with an inflatable flamigo replacing the mask" /> |

</div>

<div className="images-edit-prompt body-small">
  提示詞：一個陽光充足的室內休息區，帶有一個有天鵝泳圈的游泳池
</div>

#### 遮罩需求

要編輯的圖片與遮罩必須是相同格式與大小（大小須小於 50MB）。

遮罩圖片也必須包含 alpha channel。如果你是使用圖片編輯工具來建立遮罩，請務必將遮罩儲存為含有 alpha channel 的格式。

你可以透過程式化方式修改黑白圖片來新增 alpha channel。

為黑白遮罩新增 alpha channel

```python
from PIL import Image
from io import BytesIO

# 1. Load your black & white mask as a grayscale image
mask = Image.open(img_path_mask).convert("L")

# 2. Convert it to RGBA so it has space for an alpha channel
mask_rgba = mask.convert("RGBA")

# 3. Then use the mask itself to fill that alpha channel
mask_rgba.putalpha(mask)

# 4. Convert the mask into bytes
buf = BytesIO()
mask_rgba.save(buf, format="PNG")
mask_bytes = buf.getvalue()

# 5. Save the resulting file
img_path_mask_alpha = "mask_alpha.png"
with open(img_path_mask_alpha, "wb") as f:
    f.write(mask_bytes)
```


### 圖片輸入保真度

`input_fidelity` 參數會控制模型在編輯與參考圖片工作流程中，保留輸入圖片細節的強度。對於 `gpt-image-2`，請省略此參數；API 不允許變更它，因為模型會自動以高保真度處理每張圖片輸入。

由於 `gpt-image-2` 一律以高保真度處理圖片輸入，因此
  當編輯請求包含參考圖片時，圖片輸入 token 可能會較高。
  若要了解成本影響，請參考 [vision
  costs](https://developers.openai.com/api/docs/guides/images-vision?api-mode=responses#calculating-costs)
  章節。

## 自訂影像輸出

你可以設定以下輸出選項：

- **Size**：影像尺寸（例如，`1024x1024`、`1024x1536`）
- **Quality**：渲染品質（例如，`low`、`medium`、`high`）
- **Format**：檔案輸出格式
- **Compression**：JPEG 和 WebP 格式的壓縮等級（0-100%）
- **Background**：不透明或自動

`size`、`quality` 和 `background` 支援 `auto` 選項，模型會根據提示自動選擇最佳選項。

`gpt-image-2` 目前不支援透明背景。帶有
  `background: "transparent"` 的請求不支援此模型。

### 尺寸與品質選項

`gpt-image-2` 在符合下列限制時，`size` 參數可接受任何解析度。正方形影像通常是最快產生的。

<table>
  <tbody>
    <tr>
      <td>常見尺寸</td>
      <td>
        <ul>
          <li>
            <code>1024x1024</code>（正方形）
          </li>
          <li>
            <code>1536x1024</code>（橫向）
          </li>
          <li>
            <code>1024x1536</code>（直向）
          </li>
          <li>
            <code>2048x2048</code>（2K 正方形）
          </li>
          <li>
            <code>2048x1152</code>（2K 橫向）
          </li>
          <li>
            <code>3840x2160</code>（4K 橫向）
          </li>
          <li>
            <code>2160x3840</code>（4K 直向）
          </li>
          <li>
            <code>auto</code>（預設）
          </li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>尺寸限制</td>
      <td>
        <ul>
          <li>
            最大邊長必須小於或等於{" "}
            <code>3840px</code>
          </li>
          <li>
            兩邊都必須是 <code>16px</code> 的倍數
          </li>
          <li>
            長邊與短邊的比例不得超過 <code>3:1</code>
          </li>
          <li>
            總像素數必須至少為 <code>655,360</code>，且不超過{" "}
            <code>8,294,400</code>
          </li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>品質選項</td>
      <td>
        <ul>
          <li>
            <code>low</code>
          </li>
          <li>
            <code>medium</code>
          </li>
          <li>
            <code>high</code>
          </li>
          <li>
            <code>auto</code>（預設）
          </li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

若要快速草稿、縮圖和快速迭代，請使用 `quality: "low"`。這是
  最快的選項，且在你轉向
  `medium` 或 `high` 來產出最終素材之前，對許多常見使用情境都很適合。

總像素數超過 `2560x1440`（`3,686,400`），
  通常稱為 2K，的輸出都被視為實驗性功能。

### 輸出格式

Image API 會回傳 base64 編碼的影像資料。
預設格式是 `png`，但你也可以要求 `jpeg` 或 `webp`。

如果使用 `jpeg` 或 `webp`，你也可以指定 `output_compression` 參數來控制壓縮等級（0-100%）。例如，`output_compression=50` 會將影像壓縮 50%。

使用 `jpeg` 比 `png` 更快，因此如果
  你在意延遲，應優先使用此格式。

## 限制

GPT Image models（`gpt-image-2`、`gpt-image-1.5`、`gpt-image-1`，以及 `gpt-image-1-mini`）是功能強大且多用途的影像生成模型，但仍有一些限制需要注意：

- **延遲：** 複雜的提示詞可能需要最多 2 分鐘才能處理完成。
- **文字渲染：** 雖然已有顯著改善，但模型在精準文字排版與清晰度方面仍可能遇到困難。
- **一致性：** 雖然能夠產生一致的影像，模型有時仍可能難以在多次生成中維持重複出現的角色或品牌元素的視覺一致性。
- **構圖控制：** 儘管對指令的遵循能力已有提升，模型在結構化或對版面敏感的構圖中，仍可能難以精確放置元素。

### 內容審查

所有提示詞與生成的影像都會依照我們的 [content policy](https://openai.com/policies/usage-policies/) 進行過濾。

在使用 GPT Image models（`gpt-image-2`、`gpt-image-1.5`、`gpt-image-1`，以及 `gpt-image-1-mini`）進行影像生成時，你可以透過 `moderation` 參數控制審查嚴格程度。此參數支援兩個值：

- `auto`（預設）：標準過濾，旨在限制產生某些類別的可能不適合特定年齡的內容。
- `low`：較少限制的過濾。

### 支援的模型

在 Responses API 中使用影像生成時，`gpt-5` 及更新的模型應該都支援影像生成工具。[請查看你的模型的 model detail page](https://developers.openai.com/api/docs/models) 以確認你想使用的模型是否能使用影像生成工具。

## 成本與延遲

### `gpt-image-2` 輸出 tokens

對於 `gpt-image-2`，請使用計算器根據請求的 `quality` 和 `size` 估算輸出 tokens：

### `gpt-image-2` 之前的模型

`gpt-image-2` 之前的 GPT Image 模型會先產生專門的 image tokens 再生成圖片。延遲與最終成本都與渲染圖片所需的 token 數量成正比——較大的圖片尺寸與較高的品質設定會產生更多 tokens。

產生的 token 數量取決於圖片尺寸與品質：

| 品質 | 正方形 (1024×1024) | 縱向 (1024×1536) | 橫向 (1536×1024) |
| ------- | ------------------ | -------------------- | --------------------- |
| Low     | 272 tokens         | 408 tokens           | 400 tokens            |
| Medium  | 1056 tokens        | 1584 tokens          | 1568 tokens           |
| High    | 4160 tokens        | 6240 tokens          | 6208 tokens           |

請注意，您還需要計算 [input tokens](https://developers.openai.com/api/docs/guides/images-vision?api-mode=responses#calculating-costs)：提示詞的 text tokens，以及在編輯圖片時，輸入圖片的 image tokens。
由於 `gpt-image-2` 一律以高保真度處理圖片輸入，包含參考圖片的編輯請求可能會使用更多 input tokens。

請參考 [pricing page](https://developers.openai.com/api/docs/pricing#image-generation) 取得目前的
text 與 image token 價格，並使用下方的 [Calculating costs](#calculating-costs)
章節來估算請求成本。

最終成本為以下總和：

- input text tokens
- 使用 edits 端點時的 input image tokens
- image output tokens

### 計算成本

請使用下方的定價計算器來估算 GPT Image 模型的請求成本。
`gpt-image-2` 支援數千種有效解析度；下表列出
與先前 GPT Image 模型相同的尺寸以供比較。對於 GPT Image 1.5、
GPT Image 1 和 GPT Image 1 Mini，下方也列出了舊版按每張圖片計價的輸出價格表。
在估算請求的總成本時，您仍應計入 text 和 image input tokens。

較大的非正方形解析度有時在相同品質設定下，產生的輸出 tokens 會比
較小或正方形解析度更少。

<table
  style={{ borderCollapse: "collapse", tableLayout: "fixed", width: "100%" }}
>
  <thead>
    <tr>
      <th style={{ textAlign: "left", padding: "8px", width: "28%" }}>Model</th>
      <th style={{ textAlign: "left", padding: "8px", width: "14%" }}>
        Quality
      </th>
      <th style={{ padding: "8px", width: "19.33%" }}>1024 x 1024</th>
      <th style={{ padding: "8px", width: "19.33%" }}>1024 x 1536</th>
      <th style={{ padding: "8px", width: "19.34%" }}>1536 x 1024</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowSpan="3" style={{ padding: "8px", width: "28%" }}>
        GPT Image 2
        <br />
        <span style={{ fontSize: "0.875em" }}>Additional sizes available</span>
      </td>
      <td style={{ padding: "8px" }}>Low</td>
      <td style={{ padding: "8px" }}>$0.006</td>
      <td style={{ padding: "8px" }}>$0.005</td>
      <td style={{ padding: "8px" }}>$0.005</td>
    </tr>
    <tr>
      <td style={{ padding: "8px" }}>Medium</td>
      <td style={{ padding: "8px" }}>$0.053</td>
      <td style={{ padding: "8px" }}>$0.041</td>
      <td style={{ padding: "8px" }}>$0.041</td>
    </tr>
    <tr>
      <td style={{ padding: "8px" }}>High</td>
      <td style={{ padding: "8px" }}>$0.211</td>
      <td style={{ padding: "8px" }}>$0.165</td>
      <td style={{ padding: "8px" }}>$0.165</td>
    </tr>

    <tr>
      <td rowSpan="3" style={{ padding: "8px", width: "28%" }}>
        GPT Image 1.5
      </td>
      <td style={{ padding: "8px" }}>Low</td>
      <td style={{ padding: "8px" }}>$0.009</td>
      <td style={{ padding: "8px" }}>$0.013</td>
      <td style={{ padding: "8px" }}>$0.013</td>
    </tr>
    <tr>
      <td style={{ padding: "8px" }}>Medium</td>
      <td style={{ padding: "8px" }}>$0.034</td>
      <td style={{ padding: "8px" }}>$0.05</td>
      <td style={{ padding: "8px" }}>$0.05</td>
    </tr>
    <tr>
      <td style={{ padding: "8px" }}>High</td>
      <td style={{ padding: "8px" }}>$0.133</td>
      <td style={{ padding: "8px" }}>$0.2</td>
      <td style={{ padding: "8px" }}>$0.2</td>
    </tr>

    <tr>
      <td rowSpan="3" style={{ padding: "8px", width: "28%" }}>
        GPT Image 1
      </td>
      <td style={{ padding: "8px" }}>Low</td>
      <td style={{ padding: "8px" }}>$0.011</td>
      <td style={{ padding: "8px" }}>$0.016</td>
      <td style={{ padding: "8px" }}>$0.016</td>
    </tr>
    <tr>
      <td style={{ padding: "8px" }}>Medium</td>
      <td style={{ padding: "8px" }}>$0.042</td>
      <td style={{ padding: "8px" }}>$0.063</td>
      <td style={{ padding: "8px" }}>$0.063</td>
    </tr>
    <tr>
      <td style={{ padding: "8px" }}>High</td>
      <td style={{ padding: "8px" }}>$0.167</td>
      <td style={{ padding: "8px" }}>$0.25</td>
      <td style={{ padding: "8px" }}>$0.25</td>
    </tr>

    <tr>
      <td rowSpan="3" style={{ padding: "8px", width: "28%" }}>
        GPT Image 1 Mini
      </td>
      <td style={{ padding: "8px" }}>Low</td>
      <td style={{ padding: "8px" }}>$0.005</td>
      <td style={{ padding: "8px" }}>$0.006</td>
      <td style={{ padding: "8px" }}>$0.006</td>
    </tr>
    <tr>
      <td style={{ padding: "8px" }}>Medium</td>
      <td style={{ padding: "8px" }}>$0.011</td>
      <td style={{ padding: "8px" }}>$0.015</td>
      <td style={{ padding: "8px" }}>$0.015</td>
    </tr>
    <tr>
      <td style={{ padding: "8px" }}>High</td>
      <td style={{ padding: "8px" }}>$0.036</td>
      <td style={{ padding: "8px" }}>$0.052</td>
      <td style={{ padding: "8px" }}>$0.052</td>
    </tr>

  </tbody>
</table>

### 部分圖片成本

如果您想使用 `partial_images` 參數來 [串流圖片生成](#streaming)，每一張部分圖片都會額外產生 100 image output tokens。
