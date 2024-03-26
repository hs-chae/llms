Q_caption = [
    "What do you see in the image?",
    "What's visible in the picture?",
    "Can you describe what's in the photo?",
    "What details can you observe in this image?",
    "What does this picture show?",
    "How would you describe what's in this image?",
    "What elements are present in this picture?",
    "What can you tell me about what's in the image?",
    "What features stand out in this photo?",
    "Could you identify what's in the picture?",
    "What's depicted in this image?",
    "How do you interpret what's in the photo?",
    "What's your take on the contents of this image?",
    "What's captured in this photograph?",
    "What do you notice in the picture?",
    "What components can you see in the image?",
    "How would you sum up what's in the photo?",
    "What's illustrated in this picture?",
    "Can you point out what's in this image?",
    "What aspects are noticeable in this photo?",
    "What's being displayed in the picture?",
    "How do you read what's in this image?",
    "What's the content of this photograph?",
    "What do you discern in this picture?",
    "Can you make out what's in the image?",
    "What's the scene depicted in this photo?",
    "What do you perceive in this image?",
    "How would you interpret the contents of the picture?",
    "What's the subject of this photograph?",
    "Can you describe the scene in this image?"
]


Q_exists = [
    "Can you spot a <shape> in this image?",
    "Is there a <shape> visible in the picture?",
    "Does a <shape> appear in the image to you?",
    "Are you able to identify a <shape> in the image?",
    "Do you notice a <shape> within this image?",
    "Is a <shape> present in the image, in your view?",
    "Can you detect a <shape> in the image?",
    "Do you find a <shape> in this picture?",
    "Is a <shape> discernible in this image to you?",
    "Do you observe a <shape> in the picture?",
    "Can you make out a <shape> in the image?",
    "Is spotting a <shape> in the image possible for you?",
    "Do you recognize a <shape> in the image?",
    "Are you seeing a <shape> anywhere in this image?",
    "Is a <shape> making an appearance in the image?",
    "Can you see a <shape> featured in this image?",
    "Do you perceive a <shape> in this image?",
    "Is a <shape> evident to you in this image?",
    "Do you glimpse a <shape> in this picture?",
    "Is there any sign of a <shape> in the image for you?"
]


###################################################################################################
###################################################################################################
###################################################################################################
### Rephrased Answers

#length
A_l = [
    "The object stretches over a length of <length>.",
    "The image features a structure <length> long.",
    "You can see a form extending <length> in this picture.",
    "This figure is <length> in length.",
    "The entity spans a distance of <length>.",
    "The design in view stretches for <length>.",
    "This item in the image measures <length>.",
    "There's a piece <length> long in the scene.",
    "You can observe a component that's <length> long.",
    "The length of the object in focus is <length>.",
    "This image is <length> long.",
    "The subject shown extends for a length of <length>.",
    "The model is <length> long.",
    "This creation has a length of <length>.",
    "The silhouette measures <length>.",
    "The item highlighted here is <length> in length.",
    "The construct illustrated covers a length of <length>.",
    "The configuration is <length> long.",
    "The figure presented here is <length> long.",
    "The span of this image is <length>."
]




#shape and length
A_sl = [
    "A <shape> measures <length> in this depiction.",
    "This <shape> spans <length>.",
    "The <shape> in the image is <length> long.",
    "A <shape> extending <length> is featured.",
    "The length of the <shape> is <length>.",
    "You can see a <shape> of <length> here.",
    "The <shape> has a dimension of <length>.",
    "This picture shows a <shape> with a length of <length>.",
    "A <shape> with a total length of <length> is visible.",
    "The <shape> stretches over <length>.",
    "In the frame, a <shape> reaches <length>.",
    "The <shape> is measured to be <length>.",
    "A <shape> covering <length> is illustrated.",
    "The depicted <shape> has a length of <length>.",
    "This <shape> covers a distance of <length>.",
    "The image captures a <shape> that is <length> long.",
    "A <shape> with a span of <length> stands out.",
    "The <shape> in view extends for <length>.",
    "A clearly defined <shape> measures <length>.",
    "The <shape> presented is <length> in length."
]


#shape name
A_sn = [
    "The image captures a <shape> <name> in detail.",
    "You can clearly see a <shape> <name>.",
    "A <shape> <name> is the focal point of this picture.",
    "The <shape> <name> stands out prominently.",
    "This depiction showcases a <shape> <name>.",
    "A <shape> <name> dominates the scene.",
    "The artwork features a <shape> <name>.",
    "In view is a distinct <shape> <name>.",
    "The photograph highlights a <shape> <name>.",
    "A <shape> <name> is central to this image.",
    "The composition includes a <shape> <name>.",
    "This picture presents a <shape> <name>.",
    "The <shape> <name> is clearly visible.",
    "A <shape> <name> is displayed in the foreground.",
    "The design of the <shape> <name> is intricate.",
    "You can observe a <shape> <name> here.",
    "The structure of a <shape> <name> is evident.",
    "A <shape> <name> is depicted with precision.",
    "The outline of a <shape> <name> is sharp.",
    "This image reveals a <shape> <name>."
]


#shape and volume
A_sv = [
    "A <shape> with a volume of <volume> is depicted.",
    "The <shape> has a total volume of <volume>.",
    "This <shape> occupies a volume of <volume>.",
    "In the image, a <shape> with <volume> volume is featured.",
    "The volume of the <shape> is <volume>.",
    "You can see a <shape> holding <volume>.",
    "A <shape> encompassing <volume> is visible.",
    "The <shape> in this picture has a volume of <volume>.",
    "A <shape> filled with <volume> stands out.",
    "This picture shows a <shape> of <volume> volume.",
    "The <shape> contains a volume of <volume>.",
    "A <shape> with a capacity of <volume> is illustrated.",
    "The <shape> is volumetrically <volume>.",
    "A <shape> with a spacious <volume> is captured.",
    "The image highlights a <shape> with a volume of <volume>.",
    "This <shape> has an internal volume of <volume>.",
    "A <shape> that holds <volume> is central to the scene.",
    "The <shape> showcased has a volume of <volume>.",
    "In view is a <shape> with a volume totaling <volume>.",
    "A voluminous <shape> with <volume> is presented."
]

#two shapes
A_s2 = [
    "The composition features both a <shape1> and a <shape2>.",
    "In the foreground, a <shape1>; in the background, a <shape2>.",
    "Dominating the scene are a <shape1> alongside a <shape2>.",
    "We see a stark contrast between the <shape1> and the <shape2>.",
    "A <shape1> merges seamlessly with a <shape2> in this artwork.",
    "The image juxtaposes a vivid <shape1> against a subtle <shape2>.",
    "Foregrounded is a <shape1>, with a <shape2> providing balance.",
    "A dynamic <shape1> intersects with a static <shape2>.",
    "The focus shifts from a detailed <shape1> to a minimalist <shape2>.",
    "A <shape1> casts a shadow, hinting at the presence of a <shape2>.",
    "Intricately linked are the forms of a <shape1> and a <shape2>.",
    "A <shape1> encircles a central, commanding <shape2>.",
    "The piece showcases a <shape1> enveloping a smaller <shape2>.",
    "A <shape1> stands out, complemented by an understated <shape2>.",
    "A harmonious blend of a <shape1> with a contrasting <shape2> is observed.",
    "The narrative transitions from a <shape1> to an emerging <shape2>.",
    "A <shape1> serves as the foundation, supporting an intricate <shape2>.",
    "Elegantly juxtaposed are the silhouettes of a <shape1> and a <shape2>.",
    "The artwork captures the transition from a <shape1> to a <shape2>.",
    "A stark <shape1> contrasts with a blended <shape2> in the composition."
]

#shape, name and position
A_snp = [
    "A <shape> <name> sits prominently in the <position>.",
    "In the <position>, there's a <shape> <name> that catches the eye.",
    "Dominating the <position> is a <shape> <name>, commanding attention.",
    "A <shape> <name> in the <position> stands out against the backdrop.",
    "Tucked away in the <position> is a subtle <shape> <name>.",
    "The <position> features a striking <shape> <name>, drawing the gaze.",
    "A <shape> <name> occupies a central <position>, forming the focal point.",
    "Elegantly placed in the <position> is a <shape> <name>, adding depth.",
    "A <shape> <name> in the <position> provides balance to the scene.",
    "The <position> is adorned with a <shape> <name>, adding intrigue.",
    "In the <position>, a <shape> <name> offers a point of interest.",
    "A <shape> <name> positioned in the <position> anchors the composition.",
    "The <position> holds a <shape> <name>, creating a visual anchor.",
    "Nestled in the <position>, a <shape> <name> adds a unique element.",
    "A <shape> <name> in the <position> contrasts beautifully with its surroundings.",
    "The <position> is enhanced by the presence of a <shape> <name>.",
    "A <shape> <name>, strategically placed in the <position>, captivates the viewer.",
    "In the <position>, the <shape> <name> adds a layer of complexity.",
    "A <shape> <name> in the <position> harmonizes with the overall theme.",
    "The <position> is the perfect setting for the <shape> <name>, adding to the narrative."
]

#shape and color
A_sc = [
    "A <color> <shape> brings a dynamic element to the composition.",
    "A deep <color> <shape> lends an air of mystery and depth.",
    "The image is brightened by a <color> <shape>, offering a hint of vibrancy.",
    "A <color> <shape> provides a striking contrast to its surroundings.",
    "The serene <color> <shape> adds a calming presence to the scene.",
    "A <color> <shape>, subtle yet impactful, enhances the artwork's mood.",
    "The <color> <shape> is a visual anchor, grounding the composition.",
    "A <color> <shape> at the edge draws the viewer's gaze outward.",
    "The <color> <shape> is a testament to the power of simplicity in design.",
    "A <color> <shape> juxtaposed with contrasting elements creates harmony.",
    "The <color> <shape> echoes the theme of the piece, reinforcing its message.",
    "A solitary <color> <shape> symbolizes isolation amidst a bustling scene.",
    "The <color> <shape> is a beacon, guiding the viewer's eye through the artwork.",
    "A <color> <shape>, placed deliberately, balances the composition.",
    "The <color> <shape> adds a layer of texture and depth, enriching the visual experience.",
    "A radiant <color> <shape> captures the essence of the piece's emotion.",
    "The <color> <shape> stands as a monument within the landscape of the canvas.",
    "A <color> <shape>, though small, packs a powerful punch of color.",
    "The <color> <shape> serves as a metaphor, deeper than its visual appeal.",
    "A <color> <shape>, ethereal and light, adds a dreamlike quality to the piece."
]



