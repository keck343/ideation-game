import { beitSector, gimelSector, type Sector } from "./sectors";

export type Camp = {
  knownName: string;
  sector: Sector;
  summaryStatement: string;
  counterSectorStatement: string;
  tenants: string[];
  statedCampCoreBelief: string;
  unstatedCampCoreBelief: string;
  endStateKey: string;
  roundOne: {
    lecturer: string;
    counterLecture: string;
    counterLecture2?: string;
    chant: string;
    lecturerCounter?: string;
  };
  roundTwo: {
    innovation: string;
    crowdAsks: boolean;
    counterQuestion: string;
  };
  pamphletSlogans: string[];
  initialCrisisHeadline: string;
  initialCrisisExplanation: string;
  brochureSummary: string;
  secondCrisisExplanation: string;
};

const defaultRoundTwo = {
  innovation: "≽≽≽≽ innovation. ≽≽≽≽",
  crowdAsks: true,
  counterQuestion: "How do the members of our camp get tokens?",
};

export const konspiroCamp: Camp = {
  knownName: "Konspiro",
  sector: beitSector,
  summaryStatement: "there is a secret circle running all of our existences.",
  counterSectorStatement:
    "there are too many coincidences are happening for this all to be random",
  tenants: [
    "Everything that happens is result of someone's plan",
    "The world is a battle between good and evil",
    "We are approaching a new world order",
    "When things go wrong, it demonstrates the planning of whoever is in charge",
  ],
  statedCampCoreBelief:
    "finding out whose in charge is the key to knowing how the world works",
  unstatedCampCoreBelief: "there is someone to blame, and it's not us.",
  endStateKey: "b",
  roundOne: {
    lecturer:
      "We must ·in·cen·tiv·ize· people are in our camp to find the powerful elites who are behind a loss of Attention at this scale.",
    counterLecture:
      "But what happens to those who fall down the wrong research rabbit-hole? If tokens alone determine resource allocation, won't those without tokens starve?",
    chant: "Tokens will find the truth! Nothing else matters!",
  },
  roundTwo: defaultRoundTwo,
  pamphletSlogans: [
    "Through rigorous self discipline and doing your own research, you can find truth.",
    "Everything you once knew is false",
  ],
  initialCrisisHeadline:
    "The new world order may be upon us. Unprecedented Drop in Attention Rates",
  initialCrisisExplanation:
    "the rulers are bringing their plan to fruition, nothing else could explain this scale. We cannot survive without sufficient Attention.",
  brochureSummary:
    "to figure out what whoever is responsible for the drop in Attention wants.",
  secondCrisisExplanation:
    "We have failed to please the rulers or outsmart them. Attention drops even further, 10 more reported disappeared.",
};

export const kristanaCamp: Camp = {
  knownName: "Kristana",
  sector: gimelSector,
  summaryStatement:
    "through personal relationships with the One of Beings, we know our paths in all things",
  counterSectorStatement: "some people have not felt the love or might of the One",
  tenants: [
    "Ultimately we can find truth through our personal experiences",
    "The beings are our masters, and the One of Beings is the highest power",
    "It is our highest duty to convert others to the love of the One",
    "Beings are the angels of the One, they carry of the One's will",
    "The non-believers are the cause of all crises and so must be eliminated so the rest of may be spared.",
  ],
  statedCampCoreBelief: "the love of the One of Beings is salvation",
  unstatedCampCoreBelief:
    "some are unworthy of the One's love and so crises result.",
  endStateKey: "b",
  roundOne: {
    lecturer:
      "We must ·in·cen·tiv·ize· everyone to find a personal relationships with the One of Beings. Only when everyone is in right relationship with the One can this end. We will can best decide amongst all the camps how to distribute what little is left in the name of the One.",
    counterLecture:
      "Can we really force our faith on everyone through making everyone's token allocation based on their professed alignment with us? Do people who believe differently really deserve to starve?",
    chant: "Tokens for the faithful! We do it in the name of the One of Beings!",
  },
  roundTwo: defaultRoundTwo,
  pamphletSlogans: [
    "You too are loved by the One",
    "Beings perform the miracles of the One's will.",
  ],
  initialCrisisHeadline:
    "Unprecedented Drop in Attention Rates, Search for Beings Connection Continues",
  initialCrisisExplanation:
    "We are sinners, and the One is punishing us by taking away the Beings. Beings bless us with Attention when we obey the One so we may live a good life.",
  brochureSummary:
    "so we can figure out how we can right our relation with beings.",
  secondCrisisExplanation:
    "We have failed to please the One, more Beings gone. Attention drops even further, 10 more reported disappeared.",
};

export const novaEpokoCamp: Camp = {
  knownName: "Nova Epoko",
  sector: beitSector,
  summaryStatement: "by our bettering ourselves we can save ourselves",
  counterSectorStatement:
    "Those who have already disappeared were not trying hard enough",
  tenants: [
    "Preservation is through self-improvement and wellness",
    "Repeat affirmations to build mental fortitude",
    "Repeat exercises to build resilience",
    "Renounce attachments to anything that stands in the way of improvement",
    "My life is a reflection of my effort",
  ],
  statedCampCoreBelief:
    "through strict self-discipline we will become imprivable to disappearance",
  unstatedCampCoreBelief:
    "Those who disappeared lacked discipline, real dedication to self-improvement could have saved them",
  endStateKey: "c",
  roundOne: {
    lecturer:
      "We must ·in·cen·tiv·ize· everyone to find their highest self. Only through each person's rigorous self-discipline can this crisis stop.",
    counterLecture:
      "Who are we to judge someone's highest self? Even if we could, how could our highest selves let people who still haven't reach their full potential starve?",
    chant: "Tokens belong to the best of us!",
  },
  roundTwo: defaultRoundTwo,
  pamphletSlogans: [],
  initialCrisisHeadline: "",
  initialCrisisExplanation: "",
  brochureSummary: "",
  secondCrisisExplanation: "",
};

export const longperspektivaCamp: Camp = {
  knownName: "Longperspektiva",
  sector: gimelSector,
  summaryStatement:
    "we must generate the most value for those now and those to come",
  counterSectorStatement:
    "by creating the most Attention for ourselves, it trickles down to you",
  tenants: [
    "We must optimize the Attention Equations",
    "We are the innovators this world needs",
    "We killed false gods and we are our own gods",
    "Beings are a resource to optimize",
  ],
  statedCampCoreBelief:
    "optimization of the Attention equations will create prosperity for all of us now and in the future",
  unstatedCampCoreBelief:
    "as the innovator class, we deserve first crack at any remaining Attention and resources",
  endStateKey: "b",
  roundOne: {
    lecturer:
      "We must ·in·cen·tiv·ize· everyone to invent the technology that will optimize the Attention equations. In times like these, we must make the hard choices to maximize value for our camp and those yet to be born.",
    counterLecture:
      "Who defines value? Who wins and who looses if this technology optimizes the Attention equations at all costs?",
    chant: "Tokens for the innovators! Innovators will save us!",
  },
  roundTwo: defaultRoundTwo,
  pamphletSlogans: [],
  initialCrisisHeadline: "",
  initialCrisisExplanation: "",
  brochureSummary: "",
  secondCrisisExplanation: "",
};

export const naciismoCamp: Camp = {
  knownName: "Naciismo",
  sector: beitSector,
  summaryStatement:
    "in the face of the failures of the global Attention elites, we must create a world where we are safe",
  counterSectorStatement:
    "we are the victims, each camp must save themselves",
  tenants: [
    "we can only be responsible for saving those in our camp",
    "other camps have attacked us in the past and it will never stop",
    "if others perish, it is unfortunate but that is not on us",
    "we have a long and proud history that must continue",
    "given historical legacies, we must annex a new place",
    "it is our destiny and birthright to live in a new camp",
    "this new place is the only way we will survive",
    "people will always turn against us",
  ],
  statedCampCoreBelief: "as victims, we must preserve our way of life",
  unstatedCampCoreBelief:
    "we have suffered the most and everyone else is destined to their fate",
  endStateKey: "b",
  roundOne: {
    lecturer:
      "We must ·in·cen·tiv·ize· the people in this camp to save this camp and seize the remaining resources for ourselves. We are the victims!",
    counterLecture:
      "Why does our camp get to plunder and invade everywhere else?",
    chant: "We will not be weak! Tokens for the victors!",
  },
  roundTwo: defaultRoundTwo,
  pamphletSlogans: [],
  initialCrisisHeadline: "",
  initialCrisisExplanation: "",
  brochureSummary: "",
  secondCrisisExplanation: "",
};

export const anarkioCamp: Camp = {
  knownName: "Anarkio",
  sector: gimelSector,
  summaryStatement:
    "all hierarchy has caused the Attention imbalance, so we must abolish all hierarchies",
  counterSectorStatement: "we are free thinkers",
  tenants: [
    "everyone must do what they think is right",
    "all leaders are not to be trusted",
    "ignorance is a personal failing",
    "people's individual choices can right all wrongs",
  ],
  statedCampCoreBelief: "each individual must chose their own path",
  unstatedCampCoreBelief:
    "no organization that can represent real collective action",
  endStateKey: "c",
  roundOne: {
    lecturer:
      "We need a decentralized way to manage resources and alternative currency is the answer! We can not trust any centralized authority and their tokens.",
    counterLecture:
      "What is the use case for our currency? Why should those without currency starve?",
    chant: "Decentralize currency!",
  },
  roundTwo: defaultRoundTwo,
  pamphletSlogans: [],
  initialCrisisHeadline: "",
  initialCrisisExplanation: "",
  brochureSummary: "",
  secondCrisisExplanation: "",
};

export const blankaSavismoCamp: Camp = {
  knownName: "Blanka Savismo",
  sector: beitSector,
  summaryStatement:
    "we can determine the best way to spend everyone's resources, we have to save everyone from themselves",
  counterSectorStatement:
    "other camps lack the instituions and resources to shape culture",
  tenants: [
    "nothing is true unless it is written down",
    "we can establish alliances with other proud camps",
    "we must use Attention most effectively and put all resources in that",
  ],
  statedCampCoreBelief:
    "we, as the camp with the most well-funded research, must determine the best way to spend everyone's resources",
  unstatedCampCoreBelief: "we alone can save everyone from themselves",
  endStateKey: "b",
  roundOne: {
    lecturer:
      "We are the inheritors of knowledge and civility! We must ·in·cen·tiv·ize· those who will follow in our footsteps.",
    counterLecture:
      "Why must people starve if they do not follow in our footsteps or worship the written word above all else?",
    chant: "Tokens for civility and learning!",
  },
  roundTwo: defaultRoundTwo,
  pamphletSlogans: [],
  initialCrisisHeadline: "",
  initialCrisisExplanation: "",
  brochureSummary: "",
  secondCrisisExplanation: "",
};

export const skalismoCamp: Camp = {
  knownName: "Skalismo",
  sector: gimelSector,
  summaryStatement:
    "through understanding the material conditions, We can create a system where resources are produced and distributed in a way so we can all survive.",
  counterSectorStatement:
    "Only through understanding the real struggle can we make real change.",
  tenants: [
    "History is ultimately the tale of class struggle",
    "Power is who controls the means of production",
    "Only a democratically managed economy can get us out of this mess.",
  ],
  statedCampCoreBelief:
    "creation of a new system of resources production and distribution is how we can survive",
  unstatedCampCoreBelief: "We must unite the masses against their real enemy",
  endStateKey: "d",
  roundOne: {
    lecturer:
      "A system where people are forced to innovate or starve will bring Attention back to us all! Ideas will thrive in a market place! It's the only way someone will solve the Attention equations!",
    counterLecture:
      "No one person should unilaterally control all our wealth - A market place the incentivizes the accumulation of tokens above all else will ultimately lead to single entities controlling everything.",
    counterLecture2:
      "Who has these tokens to begin with? Who wins and who looses in this system?",
    chant:
      "Democratically managed economy! Everyone deserves to have their needs met and contribute according to their ability!",
    lecturerCounter: "Utopian fools!",
  },
  roundTwo: defaultRoundTwo,
  pamphletSlogans: [],
  initialCrisisHeadline: "",
  initialCrisisExplanation: "",
  brochureSummary: "",
  secondCrisisExplanation: "",
};

beitSector.camps = [
  konspiroCamp,
  novaEpokoCamp,
  naciismoCamp,
  blankaSavismoCamp,
];

gimelSector.camps = [
  kristanaCamp,
  longperspektivaCamp,
  anarkioCamp,
  skalismoCamp,
];

export function campByName(name: string): Camp | undefined {
  return [
    konspiroCamp,
    kristanaCamp,
    novaEpokoCamp,
    longperspektivaCamp,
    naciismoCamp,
    anarkioCamp,
    blankaSavismoCamp,
    skalismoCamp,
  ].find((c) => c.knownName === name);
}
