# The IBM Rational Unified Process for System z
RUP for System z includes a succinct end-to-end process for z practitioners 
RUP for System z includes many examples of various deliverables 
RUP for System z is available as an RMC/RUP plug-in

## Introduction 
In this chapter, we discuss the purpose, the target audience, the rationale for the book, and the scope of the method. We also provide an overview of the contents, including case study examples we used during the researching and writing of this book.

### 1.1 Purpose
The purpose of this book is to introduce the System z software development community to
the newly developed Rational Unified Process (RUP) for the System z environment.
Its aim is to describe the key fundamental principles and best practices of RUP and to
demonstrate the value of applying these very same principles and practices to development
activities within the System z environment by using Rational Unified Process for System z.
By using a real System z CICS® TS application written in COBOL as a case study, the aim is
to demonstrate the key elements and steps involved in adopting the RUP for System z
process to application development in the System z environment.
The book also describes how to obtain and install the new RUP for System z plug-in created
for the Rational Method Composer (RMC), so that you can publish the method as a Web site
and further customize the method, if necessary, to suit your own organization’s needs and
preferences.
### 1.2 Audience
This IBM Redbooks publication is intended for the whole of the System z application
development community from project managers, architects and designers, to programmers
and testers alike, because it covers the full end-to-end development lifecycle for the System z
environment.
In addition, System z Development Managers and Method Designers in particular, that is,
people who are responsible for implementing methods, standards, and procedures within
their teams or organizations, might find this book more useful as a reference guide to assist
them in adapting RUP for System z to their own development environments. The intent is for
you to be able to implement RUP for System z in a manner that is most appropriate to your
own specific development environment, so that you might reap the vast benefits that are
associated with it.
### 1.3 Rationale
Although in the recent past since the 1990s, there have been several changes in methods
and processes used in the System z application development environment, they have all
largely been related to the traditional waterfall development lifecycle model. So far, it has
been a common belief that modern development methodologies, such as RUP, are
applicable only to the Object-Oriented programming world.
However, given the current frequently changing, on demand business climate in which we
live, businesses are required to be nimble, flexible, and responsive to ever changing business
needs. Therefore, we thought it timely to investigate and document how a modern, popular,
and integrated development methodology, such as RUP, can be applied to application
development in the System z environment in order to add value to the applications and
products developed for System z.
The result is this IBM Redbooks publication. This book leverages the best elements of RUP
with a specific focus on the System z development environment.
### 1.4 Scope
The RUP for System z method addresses green field development and system evolution with
architectural changes (including turning an existing capability into a Web service, for
instance) or with significant impact on existing user business processes.
Pure maintenance is out of our scope. For more information about maintenance, refer to 4.6,
“Note on maintenance projects” on page 49 for a brief discussion about maintenance projects
and refer to the RUP for Maintenance Projects plug-in at:
http://www.ibm.com/developerworks/rational/downloads/06/plugins/rmc_prj_mnt/
The RUP for Maintenance Projects plug-in provides a delivery process, tasks, and guidance
for avoiding pitfalls during a maintenance cycle and successfully delivering a product with
higher quality than the previous release.
### 1.5 Overview
The main topics of this IBM Redbooks publication are:
 - Introduction to RUP and its extension to Service-Oriented Architecture (SOA)
 - Why RUP for System z
 - RUP for System z roadmap
 - RUP for System z process essentials
 - RUP for System z end-to-end lifecycle
 - RUP for System z content elements
 - Catalog Manager case study
 - Enterprise Generation Language (EGL)
 - RUP for System z Work Breakdown Structure (WBS)
 - How to customize RUP for System z
The main topics are followed by an appendix, which contains work products of the Catalog
Manager application development case study that were generated during various iterations of
the RUP development phases. There is an appendix that provides a terminology mapping
between RUP and System z terms and another that provides information about where to
download the RUP for System z Rational Method Composer (RMC) plug-in.
#### Introduction to RUP and its extension to Service-Oriented Architecture
This chapter introduces you to the key underlying principles of RUP and its framework of
reusable method content and process building blocks. It provides an overview of the RUP
lifecycle, describing its various phases, iterations, and the purpose and goal behind each of
the phases. This chapter also describes a roadmap through the RUP when developing
service-oriented solutions.
#### Why RUP for System z
The System z environment has been around for a long time. Over the years, its developers
have been pioneers in formulating and using various application development methodologies.
So why RUP for System z? This chapter provides you with compelling reasons for why we
undertook this project of producing a RUP for System z and the value proposition that comes
with it. The RUP key principles are commercially proven approaches to software development, obtained from industry experts and from thousands of clients and development projects. So why not expose RUP to benefit the System z environment too?
#### RUP for System z roadmap
This chapter provides a roadmap, walking through each phase (inception, elaboration,
construction, and transition) of a typical System z development project.
#### RUP for System z process essentials
This chapter provides the process essentials: A brief definition of each project phase
(inception, elaboration, construction, and transition) in terms of the main goals, activities, and
milestones. For each activity, the chapter lists the corresponding key roles, tasks, output work
products, and available examples from the Catalog Manager case study. The corresponding
section of the RUP for System z Web site provides advanced System z practitioners with all
the links necessary to perform specific activities or tasks.
#### RUP for System z end-to-end lifecycle
This chapter describes the RUP for System z process from an end-to-end lifecycle
perspective. The end-to-end lifecycle can be used as a template for planning and running a
project. It provides a complete model with predefined phases, iterations, activities, and tasks.
#### RUP for System z content elements
The RUP for System z includes a large number of content elements (roles, tasks, and
artifacts). Most of these elements come from the Rational Unified Process (RUP) and its
Service-Oriented Architecture (SOA) extension. However, some content elements have been
added to the RUP for System z because they are specific to the System z environment. This
chapter presents these new content elements.
#### Catalog Manager case study
It is common knowledge that the use of a new technology is best shown by real working
examples. In this chapter, you will find a real-life case study as an example of how we put
RUP for System z into practice. The case study walks you through our development of a
COBOL CICS application, showing you actual work products and deliverables at various
levels of incremental progress and achievement, as derived during the different phases and
iterations of the method. Reading this chapter will allow you to visualize how RUP for System
z can be put into practice during application development projects in your own organization.
#### Enterprise Generation Language (EGL)
This chapter introduces the Enterprise Generation Language (EGL) and the value that this
programming language can bring to you and your organization. EGL is a high-level
procedural language that developers unfamiliar to Java™ can use to quickly develop Web,
TUI, and batch applications with data-driven business logic. EGL can also be used to
generate COBOL for your System z. EGL was designed for developers who need to focus on
the business logic of an application rather than the technology or platform on which the
application needs to run. The result is higher productivity. We used EGL in this IBM
Redbooks publication project to develop a Web client application that consumes COBOL
CICS Web Services.
#### RUP for System z Work Breakdown Structure (WBS)
The RUP for System z includes a Work Breakdown Structure that covers the whole
development lifecycle from beginning to end. This Work Breakdown Structure can be used as
a template for planning and running a project. This chapter presents the Work Breakdown
Structure for each project phase (inception, elaboration, construction, and transition).
#### How to customize RUP for System z
Finally, for any method to be practical and applicable to your own organization’s environment,
it needs to be flexible and customizable. This chapter shows you how to customize RUP for
System z to suit your own organization’s needs and preferences in order to allow you to
implement the method or parts of the method in a manner that helps you derive the most
benefit out of it.

## The IBM Rational Unified Process for System z for Beginners

## Introduction to the IBM Rational Unified Process and its extension to Service-Oriented Architecture
The IBM Rational Unified Process for System z (RUP for System z) is based on the IBM
Rational Unified Process (RUP) and its Service-Oriented Architecture (SOA) extension (RUP
for SOA). This chapter introduces RUP and RUP for SOA.
Most of the content in this chapter comes directly from RUP and RUP for SOA where you can
obtain additional introductory information.

### 2.1 Overview
The IBM Rational Unified Process (RUP) is a software engineering process framework. It
provides best practices and guidance for successful software development and a disciplined
approach to assigning tasks and responsibilities within a development organization. Its goal is
to ensure the production of high-quality software that meets the needs of its users within a
predictable schedule and budget. Figure 2-1 illustrates the overall architecture of RUP.

As shown in Figure 2-1, RUP has two dimensions:
The horizontal axis represents time and shows the lifecycle aspects of the process as it
unfolds. The lifecycle is divided into four phases: inception, elaboration, construction, and
transition. Each phase is divided into one or more iterations. For instance, in Figure 2-1,
inception has one iteration, elaboration has two iterations, construction has n iterations,
and transition has two iterations. The right number of iterations per phase varies from
project to project.
The vertical axis represents disciplines, such as requirements, analysis, and design, or
implementation, which logically group activities by nature.

The graph shows that most iterations cover all disciplines; however, the emphasis varies over
time. For example, in early iterations you spend more time on requirements; in later iterations,
you spend more time on implementation.
This introduction to RUP and its SOA extension includes the following content:
- Introduction to RUP
  This section answers fundamental questions about the nature and purpose of RUP. 
- Key principles for successful software development
  This section presents key principles characterizing the industry’s best practices in the creation, deployment, and evolution of software-intensive systems. RUP is based on these principles.
- RUP lifecycle
  This section describes the phases and milestones of a typical RUP project lifecycle.
- Developing service-oriented solutions
  This section describes a roadmap through RUP when developing service-oriented solutions. 

### 2.2 Introduction to RUP
This section introduces the IBM Rational Unified Process (RUP) by describing the heart of
RUP and the IBM Rational Method Composer (RMC) platform.
### 2.2.1 The heart of RUP
At its heart, the IBM Rational Unified Process (RUP) is about successful software
development. There are three central elements that define RUP:
- An underlying set of philosophies and principles for successful software development
  These philosophies and principles are the foundation on which RUP has been developed. See 2.3, “Key principles for successful software development” on page 14 for more on the topic.
- A framework of reusable method content and process building blocks
  Defined and improved on an ongoing basis by Rational Software, the RUP family of method plug-ins defines a method framework from which you create your own method configurations and tailored processes.
- The underlying method and process definition language
  Underlying it all is a unified method architecture meta-model. This model provides a language for describing method content and processes. This new language is a unification of different method and process engineering languages, such as the SPEM extension to the Unified Modeling Language (UML) for software process engineering, the languages used for RUP v2003, Unified Process, IBM Global Services Method, as well as IBM Rational Summit® Ascendant.
One of the core practices behind RUP is iterative and incremental development. This practice
is also good to keep in mind as you start with RUP: Do not try to “do” all of RUP at once.
Adopt an approach to implementing, learning, and using RUP that is itself iterative and
incremental. Start by assessing your existing process and selecting one or two key areas that
you want to improve. Begin using RUP to improve these areas first and then, in later
iterations or development cycles, make incremental improvements in other areas.
### 2.2.2 The IBM Rational Method Composer (RMC) platform
Over many years of development effort, RUP has evolved into a rich process engineering
platform called IBM Rational Method Composer (RMC). RMC enables teams to define,
configure, tailor, and practice a consistent process. 

The key elements of the platform are:
- Method delivery tool
  RUP is delivered to practitioners as an interactive Web site using industry-standard browser technology. A RUP Web site is a Rational Method Composer-published process presentation configured for your project and tailored to your specific needs. The Web site is created using dynamically generated HTML pages, which RMC enables you to publish in the form of multiple RUP Web sites, each representing a configured and tailored process definition.
- Method configuration tool
  IBM Rational Method Composer (RMC) supports the fine-grained publish-time configuration of method content and processes to meet the varied needs of different projects and users. RMC allows the optional inclusion of method and process extensions using Method Composer’s plug-in technology. It also allows you to configure variants on processes, which are published differently depending on user-specific selections.
- Method authoring tool
  The IBM Rational Method Composer (RMC) tool is specifically designed for method content management and process authoring with functions, such as form-based authoring, breakdown structure-based authoring, content browsing, content search, and import and export of method content. RMC also provides mechanisms for rapid process assembly using process patterns and reusable method elements. It supports the creation of method plug-ins that provide powerful ways of extending and modifying existing content, simplifying method content, process management, and maintenance.
- A marketplace for process extensions
  The RMC/RUP section of the developerWorks® Rational Web site provides a place for process engineers in the software development community to share their method extensions as consumable plug-ins and provides a rich source of method extensions for the project manager. 
### 2.3 Key principles for successful software development
This section presents key principles characterizing the industry’s best practices in the
creation, deployment, and evolution of software-intensive systems. RUP is based on these
principles, and they are the following:
- Adapt the process.
- Balance competing stakeholder priorities.
- Collaborate across teams.
- Demonstrate value iteratively.
- Elevate the level of abstraction.
- Focus continuously on quality. 
Each principle is presented through:
- The benefits derived from applying the principle.
- The pattern of behavior that best embodies the principle.
- The most recognizable “anti-patterns” or behaviors contrary to the principle that can harm software development projects.

#### 2.3.1 Adapt the process
This principle states that it is critical to rightsize the development process to the needs of the
project. More is not better, less is not better: Instead, the amount of ceremony, precision, and
control present in a project must be tailored according to a variety of factors, including the
size and distribution of teams, the amount of externally imposed constraints, and the phase
the project is in.
Benefits:
 - Lifecycle efficiency
 - Increased project agility
 - Realistic plans and estimates
Pattern:
- Rightsize the process to project needs, including:
	- The size and distribution of the project team
	- The complexity of the application
	- The need for compliance
- Adapt process ceremony to the lifecycle phase (allow formality to evolve from light to heavy as uncertainties are resolved).
- Improve the process continuously.
- Balance plans and estimates with the level of uncertainty.
Anti-patterns:
- Always see more process and more detailed up front planning as better:
	- Force early estimates and stick to those estimates.
	- Develop precise plans, and manage the project by tracking against a static plan. 

#### 2.3.2 Balance competing stakeholder priorities
This principle articulates the importance of balancing often conflicting business and
stakeholder needs, as well as balancing custom development against asset reuse in the
satisfaction of these needs.
Benefits:
 - Align applications with business and user needs.
 - Reduce custom development.
 - Optimize business value.
Pattern:
 - Define, understand, and prioritize business and user needs.
 - Prioritize projects and requirements and couple the needs with the software capabilities.
 - Understand what assets we can leverage.
 - Balance asset reuse with user needs. 

**Анти-паттерны:**

- Тщательно документировать точные требования в начале проекта и принуждать заинтересованные стороны к их принятию.
- Согласовывать любые изменения требований, где каждое изменение может увеличить стоимость или сроки проекта.
- Жёстко фиксировать требования заранее, тем самым снижая возможность использования существующих активов.
- В основном выполнять кастомную разработку.
- Архитектурить систему только для удовлетворения потребностей самых активных заинтересованных сторон.

#### 2.3.3 Сотрудничество между командами

Этот принцип подчеркивает важность налаживания оптимальной коммуникации в масштабах всего проекта. Это достигается за счет правильной организации команд и создания эффективной совместной среды.

**Преимущества:**
- Производительность команды.
- Лучшая связь между бизнес-потребностями, разработкой и эксплуатацией программных систем.

**Паттерн:**
- Мотивировать людей работать с максимальной отдачей.
- Создавать самоуправляемые команды.
- Поощрять кросс-функциональное сотрудничество (например, между аналитиками, разработчиками и тестировщиками).
- Обеспечивать эффективную совместную среду.
- Управлять развивающимися артефактами и задачами для улучшения сотрудничества, отслеживания прогресса и понимания качества с помощью интегрированных сред.
- Интегрировать бизнес-, программные и эксплуатационные команды.

**Анти-паттерны:**
- Воспитывать героических разработчиков, готовых работать сверхурочно, включая выходные.
- Иметь узкоспециализированных сотрудников, оснащенных мощными инструментами для выполнения своей работы, с ограниченным взаимодействием между различными членами команды и ограниченной интеграцией между различными инструментами. Предполагается, что если каждый просто выполняет свою работу, конечный результат будет хорошим.

#### 2.3.4 Демонстрировать ценность итеративно

Этот принцип объясняет, почему разработка программного обеспечения значительно выигрывает от итеративности. Итеративный процесс позволяет легко адаптироваться к изменениям, получать обратную связь и учитывать ее в проекте, снижать риски на раннем этапе и динамически корректировать процесс.

**Преимущества:**
- Раннее снижение рисков.
- Высокая предсказуемость на протяжении всего проекта.
- Доверие среди заинтересованных сторон.

**Паттерн:**
- Обеспечивать обратную связь, предоставляя инкрементную пользовательскую ценность на каждой итерации.
- Адаптировать планы, используя итерационный процесс.
- Принимать изменения и управлять ими.
- Атаковать основные технические, бизнес- и программные риски на раннем этапе.

**Анти-паттерны:**
- Детально планировать весь жизненный цикл и отслеживать отклонения от плана (что на самом деле может способствовать провалу проекта).
- Оценивать статус в первые две трети проекта, полагаясь на обзоры спецификаций, а не на оценку статуса результатов тестирования и демонстрации рабочего программного обеспечения.

#### 2.3.5 Повышение уровня абстракции

Сложность является центральной проблемой в разработке программного обеспечения. Повышение уровня абстракции помогает снизить сложность, а также объем необходимой проектной документации. Это может быть достигнуто за счет повторного использования, применения инструментов высокоуровневого моделирования и ранней стабилизации архитектуры.

**Преимущества:**
- Производительность.
- Снижение сложности.

**Паттерн:**
- Повторно использовать существующие активы.
- Использовать инструменты и языки более высокого уровня для сокращения объема производимой документации.
- Сначала сосредоточиться на архитектуре.
- Архитектурить для устойчивости, качества, понятности и контроля сложности.

**Анти-паттерны:**
- Переходить напрямую от расплывчатых высокоуровневых требований к специально созданному коду:
- Поскольку используется мало абстракций, многие обсуждения ведутся на уровне кода по сравнению с более концептуальным уровнем, что упускает множество возможностей для повторного использования, среди прочего.
- Неформально зафиксированные требования и другая информация требуют многократного пересмотра решений и спецификаций.
- Ограниченное внимание к архитектуре приводит к серьёзной переработке на поздних этапах проекта.

#### 2.3.6 Непрерывная фокусировка на качестве

Этот принцип подчеркивает, что для достижения качества необходимо заниматься им на протяжении всего жизненного цикла проекта. Итеративный процесс особенно подходит для достижения качества, поскольку он предлагает множество возможностей для измерения и корректировки.

**Преимущества:**
- Более высокое качество.
- Более раннее понимание прогресса и качества.

**Паттерн:**
- Обеспечить ответственность команды за качество продукта.
- Тестировать рано и непрерывно в соответствии с интеграцией демонстрируемых возможностей.
- Инкрементно создавать автоматизацию тестирования.

**Анти-паттерны:**
- Проводить проверку всех артефактов коллегами и завершать все модульное тестирование перед интеграционным тестированием.
- Проводить углубленную проверку коллегами всех промежуточных артефактов, что контрпродуктивно, поскольку откладывает тестирование приложения и, следовательно, выявление основных проблем.
- Завершать все модульное тестирование перед проведением интеграционного тестирования, снова откладывая выявление основных проблем.

### 2.4 Жизненный цикл RUP

В этом разделе описываются фазы типичного жизненного цикла проекта RUP.

#### 2.4.1 Фаза начального замысла (Inception Phase)

Основная цель фазы начального замысла – достичь согласия всех заинтересованных сторон относительно целей жизненного цикла проекта. Фаза начального замысла имеет значение в основном для новых проектов разработки, в которых существуют значительные бизнес-риски и риски требований, которые должны быть решены до продолжения проекта. Для проектов, ориентированных на улучшение существующей системы, фаза начального замысла короче, но все же сосредоточена на обеспечении того, что проект стоит делать и его можно сделать.

**Цели:**
Основные цели фазы начального замысла включают:

- Установление границ и объема программного обеспечения проекта, включая операционное видение, критерии приемки, что должно быть в продукте, а что нет.
- Определение критических вариантов использования системы, основных сценариев работы, которые будут определять основные компромиссы в проектировании.
- Демонстрацию, а возможно, и показ, по крайней мере, одной кандидатной архитектуры на основе некоторых из основных сценариев.
- Оценку общей стоимости и сроков выполнения всего проекта (и более детальных оценок для фазы проработки).
- Оценку потенциальных рисков (источников непредсказуемости).
- Подготовку вспомогательной среды для проекта.

**Основные виды деятельности:**
Основные виды деятельности фазы начального замысла включают:

- Формулирование границ проекта. Это включает сбор контекста и наиболее важных требований и ограничений в такой степени, чтобы можно было вывести критерии приемки конечного продукта.
- Планирование и подготовку бизнес-кейса. Оценка альтернатив для управления рисками, укомплектования персоналом, плана проекта, а также компромиссов по стоимости, срокам и прибыльности.
- Создание кандидатной архитектуры, оценка компромиссов в проектировании, а также в решениях "сделать, купить, повторно использовать", чтобы можно было оценить стоимость, сроки и ресурсы. Цель здесь – продемонстрировать осуществимость с помощью подтверждения концепции. Это может принимать форму модели, которая имитирует требуемое, или начального прототипа, который исследует области высокого риска. Усилия по прототипированию во время начального замысла должны быть ограничены получением уверенности в том, что решение возможно и что оно будет реализовано во время проработки и построения.
- Подготовка среды для проекта, оценка проекта и организации, выбор инструментов и решение, какие части процесса улучшить.

Типичная итерация в фазе начального замысла проиллюстрирована на рисунке 2-2 на странице 20.

**Веха (Milestone):**
В конце фазы начального замысла находится первая важная веха проекта или Веха целей жизненного цикла (Lifecycle Objectives Milestone). На этом этапе вы изучаете цели жизненного цикла проекта и решаете либо продолжить проект, либо отменить его.

**Критерии оценки:**
- Согласие заинтересованных сторон по определению границ и оценкам стоимости/сроков.
- Согласие, что собран правильный набор требований и что существует общее понимание этих требований.
- Согласие, что оценки стоимости/сроков, приоритеты, риски и процесс разработки являются приемлемыми.
- Все риски идентифицированы, и для каждого риска существует стратегия снижения.

Проект может быть отменен или серьезно пересмотрен, если он не достигнет этой вехи.

#### 2.4.2 Фаза проработки (Elaboration Phase)

Цель фазы проработки – зафиксировать базовую линию архитектуры системы, чтобы обеспечить стабильную основу для основной части усилий по проектированию и реализации в фазе построения. Архитектура развивается на основе рассмотрения наиболее значимых требований (тех, которые сильно влияют на архитектуру системы) и оценки рисков. Стабильность архитектуры оценивается с помощью одного или нескольких архитектурных прототипов.

**Цели:**
Основные цели фазы проработки включают:

- Обеспечить, чтобы архитектура, требования и планы были достаточно стабильными, а риски достаточно снижены, чтобы можно было предсказуемо определить стоимость и сроки завершения разработки. Для большинства проектов прохождение этой вехи также соответствует переходу от быстрой, низкорисковой операции к дорогостоящей, высокорисковой операции со значительной организационной инерцией.
- Решить все архитектурно значимые риски проекта.
- Установить базовую линию архитектуры, выведенную из решения архитектурно значимых сценариев, которые обычно выявляют основные технические риски проекта.
- Создать эволюционный прототип компонентов производственного качества, а также, возможно, один или несколько исследовательских, "одноразовых" прототипов для снижения конкретных рисков, таких как: компромиссы дизайн/требования, повторное использование компонентов, осуществимость продукта или демонстрации инвесторам, клиентам и пользователям.
- Продемонстрировать, что базовая архитектура будет поддерживать требования системы с разумными затратами и в разумные сроки.
- Установить вспомогательную среду.

**Основные виды деятельности:**
Основные виды деятельности фазы проработки включают:

- Определение, валидацию и базовое закрепление архитектуры как можно быстрее.
- Уточнение видения на основе новой информации, полученной во время фазы, установление четкого понимания наиболее критических вариантов использования, которые определяют архитектурные и плановые решения.
- Создание и базовое закрепление детальных планов итераций для фазы построения.
- Уточнение процесса разработки и создание среды разработки, включая процесс, инструменты и поддержку автоматизации, необходимые для команды построения.
- Уточнение архитектуры и выбор компонентов. Потенциальные компоненты оцениваются, и решения о создании, покупке и повторном использовании достаточно понятны, чтобы с уверенностью определить стоимость и сроки фазы построения. Выбранные архитектурные компоненты интегрируются и оцениваются на соответствие основным сценариям. Уроки, извлеченные из этих мероприятий, вполне могут привести к перепроектированию архитектуры с учетом альтернативных проектов или пересмотра требований.

Типичная итерация в фазе проработки проиллюстрирована на рисунке 2-3 на странице 22.

**Веха (Milestone):**
В конце фазы проработки находится вторая важная веха проекта – Веха архитектуры жизненного цикла (Lifecycle Architecture Milestone). На этом этапе вы изучаете детальные цели и границы системы, выбор архитектуры и разрешение основных рисков.

**Критерии оценки:**
- Видение продукта и требования стабильны.
- Архитектура стабильна.
- Ключевые подходы, используемые в тестировании и оценке, доказаны.
- Тестирование и оценка исполняемых прототипов продемонстрировали, что основные элементы риска были решены и достоверно устранены.
- Планы итераций для фазы построения достаточно детализированы и точны, чтобы позволить работе продолжаться.
- Планы итераций для фазы построения подкреплены достоверными оценками.
- Все заинтересованные стороны согласны, что текущее видение может быть достигнуто, если текущий план будет выполнен для разработки полной системы в контексте текущей архитектуры.
- Фактические затраты ресурсов по сравнению с запланированными являются приемлемыми.

Проект может быть прекращен или серьезно пересмотрен, если он не достигнет этой вехи.

#### 2.4.3 Фаза построения (Construction Phase)

Цель фазы построения – уточнить оставшиеся требования и завершить разработку системы на основе базовой архитектуры. Фаза построения в некотором смысле является производственным процессом, где акцент делается на управлении ресурсами и контроле операций для оптимизации затрат, сроков и качества. В этом смысле управленческое мышление претерпевает переход от развития интеллектуальной собственности во время начального замысла и проработки к разработке развертываемых продуктов во время построения и перехода.

**Цели:**
Основные цели фазы построения включают:

- Минимизацию затрат на разработку путем оптимизации ресурсов и избежания ненужных потерь и переделок.
- Достижение адекватного качества как можно быстрее.
- Достижение полезных версий (альфа, бета и других тестовых релизов) как можно быстрее.
- Завершение анализа, проектирования, разработки и тестирования всей требуемой функциональности.
- Итеративную и инкрементную разработку готового продукта, который готов к переходу к пользовательскому сообществу. Это подразумевает описание оставшихся вариантов использования и других требований, детализацию проектирования, завершение реализации и тестирование программного обеспечения.
- Решение, готовы ли программное обеспечение, площадки и пользователи к развертыванию приложения.
- Достижение некоторой степени параллелизма в работе команд разработки. Даже в небольших проектах обычно есть компоненты, которые могут быть разработаны независимо друг от друга, что позволяет обеспечить естественный параллелизм между командами (при наличии ресурсов). Этот параллелизм может значительно ускорить разработку, но также увеличивает сложность управления ресурсами и синхронизации рабочих процессов. Надежная архитектура необходима, если необходимо достичь какого-либо значительного параллелизма.

**Основные виды деятельности:**
Основные виды деятельности фазы построения включают:

- Управление ресурсами, контроль и оптимизацию процессов.
- Полную разработку и тестирование компонентов в соответствии с определенными критериями оценки.
- Оценку релизов продукта по критериям приемки для видения.

Типичная итерация в фазе построения проиллюстрирована на рисунке 2-4 на странице 24.

**Веха (Milestone):**
На вехе первоначальной операционной готовности (Initial Operational Capability Milestone) продукт готов к передаче команде перехода. Вся функциональность разработана, и все альфа-тестирование (если таковое было) завершено. Помимо программного обеспечения, разработано руководство пользователя и есть описание текущего релиза.

**Критерии оценки:**
Критерии оценки для фазы построения включают ответы на эти вопросы:

- Достаточно ли стабилен и зрел этот релиз продукта для развертывания в пользовательском сообществе?
- Готовы ли все заинтересованные стороны к переходу в пользовательское сообщество?
- Приемлемы ли фактические затраты ресурсов по сравнению с запланированными?

Переход, возможно, придется отложить на один релиз, если проект не достигнет этой вехи.

#### 2.4.4 Фаза перехода (Transition Phase)

Основное внимание фазы перехода направлено на обеспечение доступности программного обеспечения для пользователей. Фаза перехода может охватывать несколько итераций и включает тестирование продукта в рамках подготовки к выпуску и внесение незначительных корректировок на основе отзывов пользователей. На этом этапе жизненного цикла отзывы пользователей должны быть сосредоточены в основном на тонкой настройке продукта, конфигурации, установке и проблемах удобства использования, поскольку все основные структурные проблемы должны были быть решены гораздо раньше в жизненном цикле проекта.

**Цели:**
К концу фазы перехода цели жизненного цикла должны быть достигнуты, и проект должен быть готов к завершению. В некоторых случаях окончание текущего жизненного цикла может совпадать с началом другого жизненного цикла того же продукта, ведущего к следующему поколению или версии продукта. Для других проектов окончание перехода может совпадать с полной поставкой артефактов третьей стороне, которая может отвечать за эксплуатацию, обслуживание и улучшения поставленной системы.

Эта фаза перехода варьируется от очень простой до чрезвычайно сложной, в зависимости от типа продукта. Новый релиз существующего настольного продукта может быть очень простым, тогда как замена национальной системы управления воздушным движением может быть чрезвычайно сложной.

Виды деятельности, выполняемые во время итерации в фазе перехода, зависят от цели. Например, при исправлении ошибок обычно достаточно реализации и тестирования. Однако если нужно добавить новые функции, итерация аналогична итерации в фазе построения, требующей анализа, проектирования и так далее.

Фаза перехода начинается, когда базовая линия достаточно зрела для развертывания в пользовательской среде. Обычно для этого требуется, чтобы некоторое полезное подмножество системы было завершено с приемлемым уровнем качества и пользовательской документацией, чтобы переход к пользователю принес положительные результаты для всех сторон.

Основные цели фазы перехода включают:

- Бета-тестирование для проверки новой системы в соответствии с ожиданиями пользователей.
- Бета-тестирование и параллельная эксплуатация по отношению к существующей системе, которую она заменяет.
- Конвертация операционных баз данных.
- Обучение пользователей и тех, кто будет обслуживать новую систему.
- Внедрение в отделы маркетинга, дистрибуции и продаж.
- Инжиниринг, специфичный для развертывания, такой как переход, коммерческая упаковка и производство, внедрение продаж и обучение полевого персонала.
- Деятельность по настройке, такая как исправление ошибок, улучшение производительности и удобства использования.
- Оценка базовых линий развертывания в сравнении с полным видением и критериями приемки продукта.
- Достижение возможности самообслуживания пользователей.
- Достижение согласия заинтересованных сторон в том, что базовые линии развертывания завершены.
- Достижение согласия заинтересованных сторон в том, что базовые линии развертывания соответствуют критериям оценки видения.

**Основные виды деятельности:**
Основные виды деятельности фазы перехода включают:

- Выполнение планов развертывания.
- Завершение материалов поддержки пользователей.
- Тестирование поставляемого продукта на площадке разработки.
- Создание релиза продукта.
- Получение отзывов пользователей.
- Тонкая настройка продукта на основе отзывов.
- Предоставление продукта пользователям.

Типичная итерация в фазе перехода проиллюстрирована на рисунке 2-5.

**Веха (Milestone):**
В конце фазы перехода находится четвертая важная веха проекта – Веха выпуска продукта (Product Release Milestone). На этом этапе вы решаете, были ли достигнуты цели, и нужно ли начинать другой цикл разработки. В некоторых случаях эта веха может совпадать с концом фазы начального замысла для следующего цикла. Веха выпуска продукта является результатом проверки и принятия клиентом проектных результатов.

**Критерии оценки:**
Основные критерии оценки фазы перехода включают ответы на эти вопросы:

- Удовлетворен ли пользователь?
- Приемлемы ли фактические затраты ресурсов по сравнению с запланированными?

На вехе выпуска продукта продукт находится в производстве, и начинается цикл поддержки после выпуска. Это может включать начало нового цикла или дополнительный релиз поддержки.

### 2.5 Разработка сервисно-ориентированных решений

В этом разделе описывается дорожная карта RUP при разработке сервисно-ориентированных решений, как определено в RUP для SOA. Представленный метод называется RUP/SOMA.

Метод SOMA (Service-Oriented Modeling and Architecture) был разработан как модель взаимодействия в группе IBM Global Business Services, и хотя общедоступные документы и описания были доступны, он в основном использовался консультантами в полевых условиях и не был доступен клиентам IBM. Однако RUP является коммерческим продуктом IBM, который клиенты используют для разработки собственных процессов разработки программного обеспечения. Это комплексное методологическое предложение, RUP/SOMA, было разработано, чтобы привнести уникальные аспекты SOMA в коммерческий метод RUP и сделать их доступными для коммерческих клиентов.

#### 2.5.1 Идентификация сервисов (Service Identification)

Идентификация сервисов – это в основном набор видов деятельности на этапе проработки, сосредоточенный на идентификации кандидатов в сервисы из набора активов как от бизнеса, так и от ИТ.

Задачи, идентифицированные в этом наборе видов деятельности, это:

- Задача: Анализ функциональной области.
- Задача: Уточнение бизнес-варианта использования.
- Задача: Анализ бизнес-процесса.
- Задача: Анализ бизнес-варианта использования (SOA).
- Задача: Идентификация бизнес-целей и ключевых показателей эффективности (КПЭ).
- Задача: Идентификация и привязка сервисов к целям.
- Задача: Анализ существующих активов.
- Задача: Анализ модели данных.
- Задача: Анализ бизнес-правил.
- Задача: Создание архитектурного подтверждения концепции (SOA).

#### 2.5.2 Спецификация сервисов (Service Specification)

Спецификация сервисов – это в основном набор видов деятельности на этапе проработки, сосредоточенный на выборе кандидатов в сервисы, которые будут разработаны в полные сервисы. Затем эти сервисы распределяются по подсистемам, также идентифицированным выше, и затем декомпозируются в наборы компонентов для реализации.

Задачи, идентифицированные в этом наборе видов деятельности, это:

- Задача: Применение контрольных вопросов для сервисов.
- Задача: Спецификация сервиса.
- Задача: Проектирование сообщений.
- Задача: Идентификация шаблонов безопасности.
- Задача: Проектирование подсистем (SOA).
- Задача: Спецификация компонента (SOA).

#### 2.5.3 Реализация сервисов (Service Realization)

Реализация сервисов – это в основном набор видов деятельности на этапе построения, сосредоточенный на завершении проектирования компонентов, готовых к реализации компонентов.

Задачи, идентифицированные в этом наборе видов деятельности, это:

- Задача: Документирование решений по реализации сервиса.
- Задача: Спецификация компонента (SOA).
- Задача: Создание архитектурного подтверждения концепции (SOA).

#### 2.5.4 Модель сервисов (Service Model)

В SOMA модель сервисов описывается с помощью рисунка 2-10; это единый рабочий продукт на основе документа, который охватывает различные технические и жизненные циклы представления идентифицированных и специфицированных сервисов в ходе проекта.

Артефакт RUP: Модель сервисов описывается как в форме документа, так и в форме UML, хотя более вероятно, что проект будет использовать элементы обеих этих форм для представления результатов своей работы.

### 3. Зачем нужен IBM Rational Unified Process для System z

В этой главе мы обсуждаем причины и обоснование создания RUP для System z. Мы также описываем основные различия между более старой моделью каскадной разработки и итерационной моделью разработки RUP. И, наконец, мы описываем эволюцию RUP для System z.

#### 3.1 Разработка программного обеспечения для мейнфреймов: Ключевая бизнес-возможность

Все больше и больше предприятий сегодня полагаются на серверы мейнфреймов для поддержки своего преобразования в предприятия по требованию. System z обеспечивает бизнес-интеграцию и устойчивость бизнеса: весьма желательные и необходимые возможности в современном мире по требованию. Он предоставляет предприятиям возможность динамически реагировать на меняющиеся бизнес-условия, будучи более гибкими и отзывчивыми к изменениям.

С потребностью в гибкости и отзывчивости возникает необходимость и ответственность по предоставлению поддерживающих приложений и систем для удовлетворения потребностей пользователей. Поставка приложений и систем должна быть как своевременной, так и стабильного качества. Кроме того, приложения, которые мы создаем, должны точно удовлетворять требованиям, чтобы пользователи получали именно то, что им нужно для оптимального достижения своих бизнес-целей.

#### 3.2 Разработка приложений для System z: Традиция

System z и его разработчики приложений существуют, возможно, больше лет, чем их коллеги в других средах. System z и его разработчики приложений давно являются пионерами в создании и следовании методологиям разработки приложений, признавая, что процесс является необходимым и важным элементом для последовательного производства качественного программного обеспечения. Традиционно и даже сегодня методы и процессы, используемые в среде разработки System z, обычно основаны на каскадной модели жизненного цикла.

Каскадная модель, как следует из названия, заимствована из каскадных эффектов водопада с четким началом и концом, с упорядоченным количеством фаз между ними, от сбора и анализа требований, проектирования, реализации и интеграции, заканчивая тестированием в самом конце. Фаза не начинается до завершения предыдущего этапа.

При подходе каскадной модели обычно есть только две точки взаимодействия с пользователем: первая – на этапе сбора требований, а другая – на заключительном этапе развертывания, когда решение или продукт приложения передается пользователям. Очевидно, что в конце могут быть и обычно есть сюрпризы в том, что потребности пользователей были точно удовлетворены.

#### 3.3 Что иначе

С течением времени и изменением бизнес-требований старые методы и процессы начинают проявлять недостатки. Несколько основных недостатков каскадной модели находятся в областях сбора требований и развертывания продукта. Оба недостатка связаны с тем, что каскадная модель является линейной моделью, что означает, что когда одна фаза или дисциплина завершена, проект переходит к следующей фазе.

Проблема с дисциплиной требований в каскадной модели заключается в том, что она обычно выполняется один раз в начале проекта, на основе чего строится продукт или приложение. Проходит значительное количество времени между взаимодействием и вводом от пользователя для получения требований до момента, когда продукт построен, протестирован и поставлен. К тому времени, скорее всего, потребности пользователей изменились, чтобы идти в ногу с текущей климатической ситуацией часто меняющихся бизнес-условий. Основная проблема здесь – неспособность легко адаптироваться к меняющимся требованиям пользователей.

Проблема с развертыванием в каскадной модели заключается в том, что обычно есть только один результат, передаваемый пользователю в виде конечного продукта, который поставляется в самом конце цикла разработки. Эта практика, как упоминалось ранее, создает причину для сюрпризов, потому что потребности пользователей точно не удовлетворяются.

RUP решает эти же недостатки и предоставляет множество других преимуществ. Вместо того чтобы предписывать последовательность действий "спланировать-построить-собрать" для проекта программного обеспечения, RUP является итерационным, инкрементальным процессом, который быстрее направляет команды разработчиков к результатам.

#### 3.4 Итерационная разработка по сравнению с каскадной: Различия и преимущества

С практиками, пропагандируемыми RUP, управление требованиями к программному обеспечению является более интерактивной деятельностью с пользователем. Требования к продукту постоянно и часто отслеживаются и проверяются в соответствии с потребностями заинтересованных сторон. Кроме того, продукт строится инкрементально, при этом самые сложные и наиболее рискованные компоненты проектируются и строятся в первую очередь, чтобы проверить с пользователем, что их требования и создаваемый продукт синхронизированы. Кроме того, из-за итерационной практики RUP другие виды деятельности по разработке, такие как тестирование и документация по продукту, реализуются с самого начала разработки, тем самым обеспечивая качество и поддержку документации ранней поставки.

Итак, вкратце, ключевые различия между каскадной и итерационной процессом RUP заключаются в следующем:

- Требования выполняются не только в начале, но и продолжаются на протяжении всего процесса, потому что требования по своей природе меняются с течением времени, и усилия по разработке должны быть согласованы с потребностями заинтересованных сторон.
- Реализация начинается раньше, чтобы обеспечить раннюю обратную связь от заинтересованных сторон, что является ключевым для обеспечения того, что мы строим правильную систему.
- Тестирование начинается раньше. Потому что чем позже обнаружение дефектов, тем дороже их исправление.
- Планы проекта уточняются на протяжении всего проекта на основе непрерывной переоценки (по крайней мере, один раз за итерацию) рисков и приоритетов.

#### 3.5 Эволюция RUP для System z

Эволюция видов деятельности, связанных с разработкой программного обеспечения, произошла за последние несколько десятилетий, и она развивалась в соответствии с требованиями времени. Однако в последнее время произошли значительные изменения в масштабах и скорости разработки программного обеспечения, а также в инструментах и языках, используемых для разработки программного обеспечения. RUP, будучи проверенным методом, основанным на принципах, которые характеризуют лучшие практики отрасли в создании, развертывании и эволюции программно-интенсивных систем, признан современным методом, позволяющим решать и справляться со всеми текущими требованиями и давлением, оказываемым на организации по разработке программного обеспечения.

RUP сам по себе является обширным хранилищем или базой знаний о лучших практиках. Его методологическое содержание состоит из задач, ролей и рабочих продуктов, которые относятся к разработке программного обеспечения в целом и применимы ко всем средам разработки.

RUP – это всеобъемлющая современная процессная структура. Он является общим по своей природе, потому что применим к любой среде разработки программного обеспечения: большой или маленькой, старой или новой. Однако существует общее мнение, что его практики применимы к более современным и новым технологиям и связанным с ними языкам программирования, например, объектно-ориентированной разработке и программированию на JAVA и так далее.

Как мы все знаем, среда System z по-прежнему является энергетическим центром отрасли, обеспечивая и приводя в действие все критически важные системы и приложения, которые поддерживают работу крупнейших современных предприятий, готовых быстро и эффективно адаптироваться к следующему раунду изменений, которые принесет будущее инноваций.

По этой причине мы сочли необходимым создать метод разработки специально для практиков System z, метод, который отражает практики разработки программного обеспечения, используемые в настоящее время в среде System z, используя при этом некоторые из современных лучших практик, охватываемых RUP.

RUP для System z предоставляет практикам конкретные рекомендации по разработке программного обеспечения и краткий сквозной процесс, предназначенный для среды System z. RUP для System z включает большой набор примеров рабочих продуктов, взятых из приложения, созданного на CICS Cobol и преобразованного в веб-сервисы. Сквозной жизненный цикл доступен в форме структуры декомпозиции работ (СДР).

### 4. Дорожная карта IBM Rational Unified Process для System z

Дорожная карта IBM Rational Unified Process для System z (RUP для System z) проходит через каждую фазу (начальный замысел, проработка, построение и переход) типичного проекта разработки для System z.

Дорожная карта RUP для System z охватывает разработку с нуля и эволюцию системы с архитектурными изменениями (включая, например, превращение существующей возможности в веб-сервис) или с существенным влиянием на существующие бизнес-процессы пользователей.

#### 4.1 Введение

Дорожная карта IBM Rational Unified Process для System z (RUP для System z) проиллюстрирована на рисунке 4-1. Дорожная карта предоставляет обзор для каждого из элементов на рисунке.

Виды деятельности, формирующие каждую итерацию на рисунке 4-1 на странице 38, могут выполняться последовательно или в любом порядке. Действительно, в RUP итерация не обязательно является последовательностью видов деятельности, а более сложной комбинацией видов деятельности, включая возможный параллелизм между видами деятельности.

#### 4.2 Обзор фазы начального замысла

Основная цель фазы начального замысла – достичь согласия всех заинтересованных сторон по целям жизненного цикла для проекта. Фаза начального замысла имеет значение в основном для новых проектов разработки, в которых существуют значительные бизнес-риски и риски требований, которые должны быть решены до продолжения проекта. Для проектов, ориентированных на улучшение существующей системы, фаза начального замысла короткая, но все еще сосредоточена на обеспечении того, что проект стоит делать и его можно сделать. Фаза начального замысла состоит из ряда итераций, завершающихся Вехой целей жизненного цикла.

##### 4.2.1 Цели начального замысла

Основные цели фазы начального замысла включают:

- Установление границ и объема программного обеспечения проекта, включая операционное видение, критерии приемки, что должно быть в продукте, а что нет.
- Определение критических вариантов использования системы, которые являются основными сценариями работы, которые будут определять основные компромиссы в проектировании.
- Демонстрацию, а возможно, и показ, по крайней мере, одной кандидатной архитектуры на основе некоторых из основных сценариев.
- Оценку общей стоимости и сроков для всего проекта (и более детальных оценок для фазы проработки).
- Оценку потенциальных рисков, которые являются источниками непредсказуемости.
- Подготовку вспомогательной среды для проекта. Это может включать адаптацию процесса для проекта, подготовку шаблонов, руководств и настройку инструментов при необходимости.

##### 4.2.2 Типичная итерация начального замысла

В этом разделе представлен обзор видов деятельности, выполняемых в типичной итерации фазы начального замысла, как показано на рисунке 4-2.

Деятельность "Задумать новый проект" переводит проект от первоначальной идеи до точки, в которой можно принять обоснованное решение о продолжении или отказе от проекта. Во время этой деятельности производится экономический анализ (Бизнес-кейс) и оцениваются риски. Бизнес-кейс, список рисков и начальное видение проверяются. Если они признаны удовлетворительными, проект официально создается и получает ограниченное разрешение (и бюджет) для начала планирования. Создается первоначальный черновик плана разработки программного обеспечения.

Деятельность "Подготовить среду проекта" подготавливает среду разработки для проекта, где среда разработки включает как процесс, так и инструменты. Эта деятельность включает создание среды, в которой может быть разработан, собран и предоставлен заинтересованным сторонам общий продукт.

Деятельность "Определить требования" охватывает определение видения проекта. Она достигает согласия по границам системы и описывает ключевые требования. Требования могут быть описаны в терминах модели вариантов использования, которая включает варианты использования и акторов. Основная цель варианта использования – зафиксировать требуемое поведение системы с точки зрения пользователя при достижении одной или нескольких желаемых целей. Вариант использования представляет одну или несколько последовательностей действий, которые выполняет система и которые дают наблюдаемый результат, имеющий ценность для конкретного актора, такого как пользователь. На этапе начального замысла идентифицируются и кратко описываются основные варианты использования. Требования (функциональные и нефункциональные), которые не подходят для вариантов использования, должны быть задокументированы в дополнительных спецификациях. После того как определено несколько вариантов использования и дополнительных требований, они приоритизируются, чтобы можно было определить порядок их разработки. Например, варианты использования, которые представляют некоторую значительную функциональность, имеют значительное архитектурное покрытие (которое затрагивает многие архитектурные элементы) или напрягают или иллюстрируют конкретную и деликатную точку архитектуры, будут разрабатываться первыми. Кроме того, термины проекта должны быть определены в Глоссарии, который будет поддерживаться на протяжении всей жизни проекта. Эта деятельность также запускает усилия по тестированию, предоставляя первый черновик плана тестирования.

Деятельность "Выполнить архитектурное подтверждение концепции" направлена на демонстрацию осуществимости решения путем создания архитектурного подтверждения концепции и оценки жизнеспособности этого архитектурного подтверждения концепции. Архитектурное подтверждение концепции может принимать различные формы, такие как набросок концептуальной модели решения с использованием нотации, такой как Unified Modeling Language (UML), имитация решения или исполняемый прототип. Архитектурное подтверждение концепции оценивается в соответствии с архитектурно значимыми требованиями. Требования, которые обычно являются архитектурно значимыми, включают производительность, масштабирование, синхронизацию процессов и потоков и распределение.

Деятельность "Спланировать проект" начинается с оценки текущей итерации и переоценки рисков. Она уточняет план разработки программного обеспечения (охватывающий все фазы и итерации проекта) и создает детализированный план итерации для следующей итерации или итераций. Эта деятельность также приобретает необходимые ресурсы (включая персонал) для выполнения предстоящей итерации или итераций.

##### 4.2.3 Веха целей жизненного цикла

В конце фазы начального замысла находится первая важная веха проекта или Веха целей жизненного цикла. На этом этапе вы изучаете цели жизненного цикла проекта и решаете либо продолжить проект, либо отменить его. В конце фазы начального замысла проект оценивается по следующим критериям:

- Согласие заинтересованных сторон по определению границ и оценкам стоимости/сроков.
- Согласие, что собран правильный набор требований и что существует общее понимание этих требований.
- Согласие, что оценки стоимости/сроков, приоритеты, риски и процесс разработки являются приемлемыми.
- Все риски идентифицированы, и для каждого риска существует стратегия снижения.

Проект может быть отменен или серьезно пересмотрен, если он не достигнет этой вехи.

**Сводка основных рабочих продуктов и их состояния в конце фазы начального замысла:**
- Бизнес-кейс (100% завершено)
- Видение (примерно 100% завершено)
- Глоссарий (примерно 40% завершено)
- План разработки программного обеспечения (примерно 80% завершено)
- План итерации для первой итерации проработки (примерно 100% завершено)
- Список рисков (примерно 25% завершено)
- Модель вариантов использования (примерно 20% завершено)
- Дополнительные спецификации (примерно 20% завершено)
- План тестирования (примерно 10% завершено)
- Документ по архитектуре программного обеспечения (примерно 10% завершено)
- Архитектурное подтверждение концепции (один или несколько прототипов подтверждения концепции доступны для решения конкретных рисков)

#### 4.3 Обзор фазы проработки

Цель фазы проработки – зафиксировать базовую линию архитектуры системы, чтобы обеспечить стабильную основу для основной части усилий по проектированию и реализации в фазе построения. Архитектура развивается на основе рассмотрения наиболее значимых требований (тех, которые сильно влияют на архитектуру системы) и оценки рисков. Стабильность архитектуры оценивается с помощью одного или нескольких архитектурных прототипов. Фаза проработки состоит из ряда итераций, завершающихся Вехой архитектуры жизненного цикла.

##### 4.3.1 Цели проработки

Основные цели фазы проработки включают:

- Обеспечить, чтобы архитектура, требования и планы были достаточно стабильны, а риски достаточно снижены, чтобы можно было предсказуемо определить стоимость и сроки завершения разработки. Для большинства проектов прохождение этой вехи также соответствует переходу от быстрой, низкорисковой операции к дорогостоящей, высокорисковой операции со значительной организационной инерцией.
- Решить все архитектурно значимые риски проекта.
- Установить базовую линию архитектуры, выведенную из решения архитектурно значимых сценариев, которые обычно выявляют основные технические риски проекта.
- Создать эволюционный прототип компонентов производственного качества, а также, возможно, один или несколько исследовательских, "одноразовых" прототипов для снижения конкретных рисков, таких как: компромиссы дизайн/требования, повторное использование компонентов, осуществимость продукта или демонстрации инвесторам, клиентам и пользователям.
- Продемонстрировать, что базовая архитектура будет поддерживать требования системы с разумными затратами и в разумные сроки.
- Уточнить вспомогательную среду.

##### 4.3.2 Типичная итерация проработки

В этом разделе представлен обзор видов деятельности, выполняемых в типичной итерации фазы проработки, как показано на рисунке 4-3.

Деятельность "Уточнить требования" касается детализации требований системы с точки зрения ее вариантов использования. Только варианты использования, которые находятся в рамках текущей итерации, детализируются для достижения цели итерации. Оставшиеся варианты использования будут детализированы в последующих итерациях. Детализация варианта использования включает описание его потока событий. Требования (функциональные и нефункциональные), которые не подходят для вариантов использования, должны быть детализированы в дополнительных спецификациях. Варианты использования и дополнительные требования продолжают приоритизироваться, чтобы можно было определить порядок их разработки. Термины проекта продолжают определяться или уточняться в Глоссарии.

Деятельность "Определить архитектуру" начинается с создания начального наброска архитектуры программного обеспечения в поддеятельности "Определить кандидативную архитектуру". Эта поддеятельность определяет кандидативную архитектуру (начальную организацию системы), использует существующие активы, определяет архитектурные шаблоны, идентифицирует архитектурно значимые варианты использования и выполняет анализ варианта использования (также называемый реализацией варианта использования) для каждой кандидатной архитектуры. Это включает идентификацию элементов анализа, необходимых для выражения поведения каждого варианта использования. Эти элементы анализа позже будут уточнены в элементы проектирования, такие как модули и классы проектирования, и исходный код. После того как кандидативная архитектура определена, деятельность "Определить архитектуру" завершает архитектуру для итерации в поддеятельности "Уточнить архитектуру". Эта поддеятельность обеспечивает естественный переход от видов деятельности анализа к видам деятельности проектирования путем идентификации соответствующих элементов проектирования из элементов анализа. Она также описывает организацию исполняемой и развертываемой архитектуры системы и поддерживает согласованность и целостность архитектуры. Деятельность заканчивается обзором полученной архитектуры, задокументированной в Документе по архитектуре программного обеспечения.

Деятельность "Спроектировать компоненты" касается детального проектирования одного или нескольких компонентов в рамках границ, определенных в плане итерации. Основными целями являются:

- Уточнить определение поведения каждого компонента с помощью взаимодействий элементов проектирования (модулей, классов, интерфейсов, событий и т.д.) или оставшихся элементов анализа.
- Идентифицировать новые элементы проектирования, анализируя эти взаимодействия.
- Разделить элементы проектирования на подсистемы и задокументировать внутреннюю структуру и поведение подсистем, их интерфейсы и зависимости. Эти подсистемы теперь могут быть уточнены и реализованы отдельно друг от друга.
- Уточнить определения элементов проектирования, проработав "детали" того, как они реализуют требуемое от них поведение.

Когда задействованы сервисы, деятельность "Спроектировать компоненты" уточняет проектирование элементами сервисов. Когда задействованы базы данных, эта деятельность идентифицирует элементы проектирования, которые должны сохраняться в базе данных, и проектирует соответствующие структуры базы данных. Когда задействован пользовательский интерфейс, эта деятельность моделирует и создает прототип пользовательского интерфейса. Эта деятельность заканчивается обзором полученного проектирования, задокументированного в Модели проектирования, и, возможно, других вспомогательных моделей, таких как Модель сервисов.

Деятельность "Кодировать и модульно тестировать компоненты" завершает часть реализации, чтобы ее можно было поставить на интеграцию. Эта деятельность реализует элементы в модели проектирования путем написания исходного кода, адаптации существующего исходного кода, компиляции, связывания и выполнения модульных тестов. Если обнаружены дефекты в проектировании, отправляется обратная связь по переработке проектирования. Деятельность также включает исправление дефектов кода и выполнение модульных тестов для проверки изменений. Код проверяется для оценки качества и соответствия руководствам по программированию.

Деятельность "Интегрировать и тестировать" охватывает интеграцию и тестирование продукта. Поддеятельность "Интегрировать" интегрирует изменения от нескольких реализаторов для создания новой согласованной версии подсистемы реализации (это делается для любой подсистемы реализации в рамках итерации) и интегрирует подсистемы реализации для создания новой согласованной версии общей системы, когда это уместно. Интегратор интегрирует систему в соответствии с планом сборки интеграции, добавляя поставленные подсистемы реализации в рабочее пространство интеграции системы и создавая сборки. Затем каждая сборка тестируется интеграционно тестировщиком. После последнего инкремента сборка может быть полностью протестирована на системном уровне. Поддеятельность "Тестировать" включает задачи, необходимые для тестирования в рамках конкретного объема. Объем может быть определенным уровнем или типом теста, таким как функциональная проверка (FVT) или системная проверка (SVT). Он также может быть ограничен компонентами или их частями, которые были реализованы или планируются к реализации во время итерации. Поддеятельность "Тестировать" включает уточнение плана тестирования, определение тестовых случаев и их реализацию в тестовых сценариях (тестовый сценарий – это пошаговая инструкция, позволяющая выполнить тестовый случай), выполнение и оценку тестов (группой тестов, называемой тестовым набором, созданным для выполнения категории тестов, такой как FVT или SVT) и соответствующее сообщение о возникших инцидентах. Она также включает определение и реализацию процедур проверки установки (IVPs).

Деятельность "Спланировать проект" начинается с оценки текущей итерации и переоценки рисков. Она уточняет план разработки программного обеспечения (охватывающий все фазы и итерации проекта) и создает детализированный план итерации для следующей итерации или итераций. Эта деятельность также приобретает необходимые ресурсы (включая персонал) для выполнения предстоящей итерации или итераций.

##### 4.3.3 Веха архитектуры жизненного цикла

В конце фазы проработки находится вторая важная веха проекта – Веха архитектуры жизненного цикла. На этом этапе вы изучаете детальные цели и границы системы, выбор архитектуры и разрешение основных рисков. В конце фазы проработки проект оценивается по следующим критериям:

- Видение продукта и требования стабильны.
- Архитектура стабильна.
- Ключевые подходы, используемые в тестировании и оценке, доказаны.
- Тестирование и оценка исполняемых прототипов продемонстрировали, что основные элементы риска были решены и достоверно устранены.
- Планы итераций для фазы построения достаточно детализированы и точны, чтобы позволить работе продолжаться.
- Планы итераций для фазы построения подкреплены достоверными оценками.
- Все заинтересованные стороны согласны, что текущее видение может быть достигнуто, если текущий план будет выполнен для разработки полной системы в контексте текущей архитектуры.
- Фактические затраты ресурсов по сравнению с запланированными являются приемлемыми.

Проект может быть прекращен или серьезно пересмотрен, если он не достигнет этой вехи.

**Сводка основных рабочих продуктов и их состояния в конце фазы проработки:**
- Глоссарий (примерно 80% завершено)
- План разработки программного обеспечения (примерно 95% завершено)
- Планы итераций для итераций построения (примерно 100% завершено, по крайней мере для первой итерации)
- Список рисков (примерно 50% завершено)
- Модель вариантов использования (примерно 80% завершено)
- Дополнительные спецификации (примерно 80% завершено)
- Документ по архитектуре программного обеспечения (примерно 100% завершено)
- Модель проектирования (примерно 60% завершено)
- Модель сервисов (примерно 60% завершено)
- План тестирования (примерно 30% завершено)
- Тестовые случаи (примерно 40% завершено)
- Тестовые сценарии (примерно 40% завершено)
- Элементы реализации, включая исходный код (примерно 40% завершено)
- Сборки доступны (одна или несколько за итерацию, например)
- Один или несколько исполняемых архитектурных прототипов доступны (для изучения критической функциональности и архитектурно значимых сценариев)
- Процедуры проверки установки (IVPs) (примерно 80% завершено)

#### 4.4 Обзор фазы построения

Цель фазы построения – завершить разработку системы на основе базовой архитектуры. Фаза построения в некотором смысле является производственным процессом, где акцент делается на управлении ресурсами и контроле операций для оптимизации затрат, сроков и качества. В этом смысле управленческое мышление претерпевает переход от развития интеллектуальной собственности во время начального замысла и проработки к разработке развертываемых продуктов во время построения и перехода. Фаза построения состоит из ряда итераций, завершающихся Вехой первоначальной операционной готовности.

##### 4.4.1 Цели построения

Основные цели фазы построения включают:

- Минимизацию затрат на разработку путем оптимизации ресурсов и избежания ненужных потерь и переделок.
- Достижение адекватного качества как можно быстрее.
- Достижение полезных версий (альфа, бета и других тестовых релизов) как можно быстрее.
- Завершение анализа, проектирования, разработки и тестирования всей требуемой функциональности.
- Итеративную и инкрементную разработку готового продукта, который готов к переходу к пользовательскому сообществу. Это подразумевает описание оставшихся вариантов использования и других требований, детализацию проектирования, завершение реализации и тестирование программного обеспечения.
- Решение, готовы ли программное обеспечение, площадки и пользователи к развертыванию приложения.
- Достижение некоторой степени параллелизма в работе команд разработки. Даже в небольших проектах обычно есть компоненты, которые могут быть разработаны независимо друг от друга, что позволяет обеспечить естественный параллелизм между командами (при наличии ресурсов). Этот параллелизм может значительно ускорить разработку, но также увеличивает сложность управления ресурсами и синхронизации рабочих процессов. Надежная архитектура необходима, если необходимо достичь какого-либо значительного параллелизма.

##### 4.4.2 Типичная итерация построения

В этом разделе представлен обзор видов деятельности, выполняемых в типичной итерации фазы построения, как показано на рисунке 4-4.

Деятельность "Уточнить требования" завершает детализацию требований системы с точки зрения вариантов использования. Требования (функциональные и нефункциональные), которые не подходят для вариантов использования, должны быть детализированы в дополнительных спецификациях. Термины проекта продолжают определяться или уточняться в Глоссарии.

Деятельность "Спроектировать компоненты" завершает детальное проектирование компонентов в рамках границ, определенных в плане итерации. Эта деятельность заканчивается обзором полученного проектирования, задокументированного в Модели проектирования, и, возможно, других вспомогательных моделей, таких как Модель сервисов.

Деятельность "Кодировать и модульно тестировать компоненты" завершает большинство частей реализации, чтобы их можно было поставить на интеграцию. Эта деятельность реализует элементы в модели проектирования путем написания исходного кода, адаптации существующего исходного кода, компиляции, связывания и выполнения модульных тестов. Код проверяется для оценки качества и соответствия руководствам по программированию.

Деятельность "Интегрировать и тестировать" охватывает интеграцию и тестирование продукта. Поддеятельность "Интегрировать" интегрирует изменения от нескольких реализаторов для создания новой согласованной версии подсистемы реализации (это делается для любой подсистемы реализации в рамках итерации) и интегрирует подсистемы реализации для создания новой согласованной версии общей системы, когда это уместно. Поддеятельность "Тестировать" включает задачи, необходимые для тестирования в рамках конкретного объема, такого как функциональная проверка (FVT) компонентов, реализованных во время итерации, или системная проверка (SVT). Она включает уточнение плана тестирования, определение тестовых случаев и их реализацию в тестовых сценариях, выполнение и оценку тестов (группой тестов, называемой тестовым набором, созданным для выполнения категории тестов, такой как FVT или SVT) и соответствующее сообщение о возникших инцидентах. Она также включает определение и реализацию процедур проверки установки (IVPs).

Деятельность "Подготовить развертывание" определяет план развертывания. Его цель – обеспечить успешное достижение системой своих пользователей. План развертывания предоставляет детальный график событий, ответственных лиц и зависимости событий, необходимых для успешного перехода на новую систему. Деятельность также включает определение первого черновика материалов поддержки пользователей и других сопутствующих материалов, охватывающих полный спектр информации, необходимой пользователю для изучения, установки, эксплуатации, использования и обслуживания системы.

Деятельность "Спланировать проект" начинается с оценки текущей итерации и переоценки рисков. Она уточняет план разработки программного обеспечения (охватывающий все фазы и итерации проекта) и создает детализированный план итерации для следующей итерации или итераций. Эта деятельность также приобретает необходимые ресурсы (включая персонал) для выполнения предстоящей итерации или итераций.

##### 4.4.3 Веха первоначальной операционной готовности

На вехе первоначальной операционной готовности продукт готов к передаче команде перехода. Вся функциональность разработана, и все альфа-тестирование (если таковое было) завершено. Помимо программного обеспечения, разработано руководство пользователя и есть описание текущего релиза. Критерии оценки для фазы построения включают ответы на эти вопросы:

- Достаточно ли стабилен и зрел этот релиз продукта для развертывания в пользовательском сообществе?
- Готовы ли все заинтересованные стороны к переходу в пользовательское сообщество?
- Приемлемы ли фактические затраты ресурсов по сравнению с запланированными затратами ресурсов?

Переход, возможно, придется отложить на один релиз, если проект не достигнет этой вехи.

**Сводка основных рабочих продуктов и их состояния в конце фазы построения:**
- Глоссарий (примерно 100% завершено)
- План разработки программного обеспечения (примерно 100% завершено)
- Планы итераций для итераций перехода (примерно 100% завершено, по крайней мере для первой итерации)
- Список рисков (примерно 75% завершено)
- Модель вариантов использования (примерно 100% завершено)
- Дополнительные спецификации (примерно 100% завершено)
- Модель проектирования (примерно 100% завершено)
- Модель сервисов (примерно 100% завершено)
- План тестирования (примерно 90% завершено)
- Тестовые случаи (примерно 80% завершено)
- Тестовые сценарии (примерно 80% завершено)
- Элементы реализации, включая исходный код (примерно 90% завершено)
- Сборки доступны (одна или несколько за итерацию, например)
- Исполняемая система доступна
- Процедуры проверки установки (IVPs) (примерно 90% завершено)
- Материалы поддержки пользователей (примерно 40% завершено)

#### 4.5 Обзор фазы перехода

Основное внимание фазы перехода направлено на обеспечение доступности программного обеспечения для пользователей. Фаза перехода может охватывать несколько итераций и включает тестирование продукта в рамках подготовки к выпуску и внесение незначительных корректировок на основе отзывов пользователей. На этом этапе жизненного цикла отзывы пользователей должны быть сосредоточены в основном на тонкой настройке продукта, конфигурации, установке и проблемах удобства использования. Все основные структурные проблемы должны были быть решены гораздо раньше в жизненном цикле проекта. Фаза перехода состоит из ряда итераций, завершающихся Вехой выпуска продукта.

##### 4.5.1 Цели перехода

Фаза перехода начинается, когда базовая линия достаточно зрела для развертывания в пользовательской среде. Это развертывание обычно требует, чтобы некоторое полезное подмножество системы было завершено с приемлемым уровнем качества и пользовательской документацией, чтобы переход к пользователю принес положительные результаты для всех сторон. Основные цели фазы перехода включают:

- Бета-тестирование для проверки новой системы в соответствии с ожиданиями пользователей.
- Бета-тестирование и параллельная эксплуатация по отношению к системе, которую она заменяет.
- Конвертация операционных баз данных.
- Обучение пользователей и тех, кто будет обслуживать систему.
- Внедрение в отделы маркетинга, дистрибуции и продаж.
- Инжиниринг, специфичный для развертывания, такой как переход, коммерческая упаковка и производство, внедрение продаж и обучение полевого персонала.
- Деятельность по настройке, такая как исправление ошибок и улучшение производительности и удобства использования.
- Оценка базовых линий развертывания в сравнении с полным видением и критериями приемки продукта.
- Достижение возможности самообслуживания пользователей.
- Достижение согласия заинтересованных сторон в том, что базовые линии развертывания завершены.
- Достижение согласия заинтересованных сторон в том, что базовые линии развертывания соответствуют критериям оценки видения.

Фаза перехода варьируется от простой до чрезвычайно сложной, в зависимости от типа продукта. Новый релиз существующего настольного продукта может быть простым, тогда как замена национальной системы управления воздушным движением может быть чрезвычайно сложной. Виды деятельности, выполняемые во время итерации в фазе перехода, зависят от цели. Например, при исправлении ошибок обычно достаточно реализации и тестирования. Однако если нужно добавить новые функции, итерация аналогична итерации в фазе построения, требующей анализа, проектирования и так далее.

##### 4.5.2 Типичная итерация перехода

В этом разделе представлен обзор видов деятельности, выполняемых в типичной итерации фазы перехода, как показано на рисунке 4-5 на странице 48.

При переходе, в некоторых случаях может быть необходимо обновить требования и проектирование системы. Однако любые значительные изменения следует отложить до будущего поколения решения, чтобы сохранить стабильность, необходимую для функциональности, полезной пользователям, и установить основу для создания будущих решений (или решения, принятые на вехе первоначальной операционной готовности, возможно, придется пересмотреть).

Деятельность "Кодировать и модульно тестировать компоненты" завершает все оставшиеся части реализации системы, чтобы их можно было поставить на интеграцию. Эта деятельность реализует элементы в модели проектирования путем написания исходного кода, адаптации существующего исходного кода, компиляции, связывания и выполнения модульных тестов. Код проверяется для оценки качества и соответствия руководствам по программированию.

Деятельность "Интегрировать и тестировать" завершает интеграцию и тестирование продукта. Поддеятельность "Интегрировать" интегрирует изменения от нескольких реализаторов для создания новой согласованной версии подсистемы реализации и интегрирует подсистемы реализации для создания новой согласованной версии общей системы. Поддеятельность "Тестировать" включает задачи, необходимые для тестирования в рамках конкретного объема, такого как системная проверка (SVT). Она включает уточнение плана тестирования, определение тестовых случаев и их реализацию в тестовых сценариях, выполнение и оценку тестов (группой тестов, называемой тестовым набором, созданным для выполнения категории тестов, такой как SVT) и соответствующее сообщение о возникших инцидентах. Она также завершает определение и реализацию процедур проверки установки (IVPs).

Деятельность "Выполнить бета- и приемочное тестирование" охватывает бета- и приемочное тестирование продукта. Поддеятельность "Выполнить бета-тестирование" запрашивает обратную связь по продукту у подмножества предполагаемых пользователей, пока он еще находится в активной разработке. Бета-тестирование дает продукту контролируемое, реальное тестирование, так что обратная связь от потенциальных пользователей может быть использована для формирования конечного продукта. Это также предоставляет предварительный просмотр следующего релиза заинтересованным клиентам. Поддеятельность "Выполнить приемочное тестирование" обеспечивает, чтобы продукт был признан приемлемым для клиента до его общего выпуска.

Деятельность "Упаковать продукт" создает и упаковывает продукт для выпуска. Она производит любые оставшиеся материалы поддержки пользователей и любые артефакты, необходимые для эффективного развертывания продукта его пользователям, такие как учебные материалы или примечания к выпуску. Она также производит единицу развертывания, которая позволяет программному продукту быть эффективно установленным и использованным. Пакет единицы развертывания состоит из сборки (исполняемой коллекции компонентов), документов, таких как материалы поддержки пользователей, и процедур проверки установки (IVPs). Единица развертывания достаточно полна, чтобы быть загруженной и запущенной на узле. Это определение подходит для случаев, когда продукт доступен через Интернет, и единица развертывания может быть загружена непосредственно и установлена пользователем. В случае "коробочного" программного обеспечения единица развертывания снабжена отдельной упаковкой, состоящей из художественного оформления и сообщений, и продается как продукт.

Деятельность "Спланировать проект" начинается с оценки текущей итерации и переоценки рисков. Когда ожидаются дополнительные итерации, она уточняет детализированный план итерации для следующей итерации или итераций. Во время последней итерации проекта подготавливается окончательная оценка статуса для обзора приемки проекта, который, если успешен, отмечает момент, когда клиент формально принимает право собственности на программный продукт. Затем руководитель проекта завершает закрытие проекта, распоряжаясь оставшимися активами и перераспределяя оставшийся персонал.

##### 4.5.3 Веха выпуска продукта

В конце фазы перехода находится четвертая важная веха проекта – Веха выпуска продукта. На этом этапе вы решаете, были ли достигнуты цели, и следует ли начинать другой цикл разработки. Веха выпуска продукта является результатом проверки и принятия клиентом проектных результатов. Основные критерии оценки фазы перехода включают ответы на эти вопросы:

- Удовлетворен ли пользователь?
- Приемлемы ли фактические затраты ресурсов по сравнению с запланированными?

На вехе выпуска продукта продукт находится в производстве, и начинается цикл поддержки после выпуска. Это может включать начало нового цикла или дополнительного релиза поддержки.

**Сводка основных рабочих продуктов, завершенных во время фазы перехода:**
- Список рисков
- План тестирования
- Тестовые случаи
- Тестовые сценарии
- Элементы реализации, включая исходный код
- Единица развертывания
- Сборка
- Материалы поддержки пользователей
- Процедуры проверки установки (IVPs)
- Продукт

К концу фазы перехода проект должен быть готов к завершению. В некоторых случаях окончание текущего жизненного цикла может совпадать с началом другого жизненного цикла того же продукта, ведущего к следующему поколению или версии продукта. Для других проектов окончание фазы перехода может совпадать с полной поставкой артефактов третьей стороне, которая может отвечать за эксплуатацию, обслуживание и улучшения поставленной системы.

#### 4.6 Примечание о проектах сопровождения

Дорожная карта RUP для System z, представленная в этой главе, охватывает разработку с нуля и эволюцию системы с архитектурными изменениями (включая, например, превращение существующей возможности в веб-сервис) или значительным влиянием на существующие бизнес-процессы пользователей. Чистое сопровождение выходит за рамки этой книги.

Основные характеристики цикла продукта сопровождения по сравнению с обычным циклом продукта разработки следующие:

- Фазы начального замысла и проработки объединены в одну итерацию, называемую Начальный замысел/Проработка.
- В цикле продукта нет архитектурных изменений, или изменения имеют документально подтвержденное незначительное влияние на существующее проектирование и бизнес-процессы пользователей.
- Процесс управляется запросами на изменения, а не требованиями или новым объемом продукта.
- Уделяется внимание рефакторингу кода, проектирования и требований для снижения долгосрочного роста сложности системы. Это известно как внесение улучшающих изменений.
- Объем продукта не изменяется и не увеличивается.
- Цикл продукта имеет те же бизнес-драйверы, что и предыдущий цикл продукта.
- Жизненный цикл носит неформальный характер, особенно в отношении проектных артефактов.

### 5. Основы процесса

В этой главе представлены основы процесса: краткое определение каждой фазы проекта (начальный замысел, проработка, построение и переход) с точки зрения основных целей, видов деятельности и вех. Для каждого вида деятельности в главе перечислены соответствующие ключевые роли, задачи, выходные рабочие продукты и доступные примеры из тематического исследования "Менеджер каталога". Соответствующий раздел веб-сайта RUP для System z предоставляет продвинутым практикам System z все необходимые ссылки (подчеркнутые термины) для выполнения конкретных видов деятельности или задач.

#### 5.1 Основы начального замысла

Основная цель фазы начального замысла – достичь согласия всех заинтересованных сторон по объему проекта и обеспечить, что проект стоит делать и его можно сделать. Фаза начального замысла состоит из ряда итераций, завершающихся Вехой целей жизненного цикла. Типичная итерация начального замысла включает виды деятельности, представленные в таблице 5-1. Веха описывается сразу после таблицы.

**Таблица 5-1. Виды деятельности типичной итерации начального замысла**

| Вид деятельности | Роли | Задачи | Выходные рабочие продукты | Примеры Менеджера каталога |
|---|---|---|---|---|
| **Задумать новый проект** | - Руководитель проекта<br>- Рецензент руководства | - Разработать бизнес-кейс<br>- Идентифицировать и оценить риски<br>- Инициировать проект<br>- Провести обзор утверждения проекта | - Бизнес-кейс<br>- План разработки ПО<br>- Список рисков<br>- Запись обзора | - Бизнес-кейс |
| **Подготовить среду проекта** | - Инженер процесса<br>- Специалист по инструментам<br>- Менеджер конфигурации | - Адаптировать процесс разработки для проекта<br>- Выбрать и приобрести инструменты<br>- Настроить инструменты<br>- Настроить среду управления конфигурацией (CM) | - Процесс разработки<br>- Инструменты<br>- Репозиторий проекта | Нет |
| **Определить требования** | - Системный аналитик<br>- Архитектор ПО<br>- Тест-дизайнер | - Разработать видение<br>- Найти акторов и варианты использования<br>- Разработать дополнительные спецификации<br>- Зафиксировать общий словарь<br>- Приоритизировать варианты использования<br>- Определить подход к тестированию | - Видение<br>- Модель вариантов использования<br>- Дополнительные спецификации<br>- Глоссарий<br>- Документ по архитектуре ПО<br>- Стратегия тестирования<br>- План тестирования<br>- Конфигурация среды тестирования | - Видение<br>- Модель вариантов использования<br>- Дополнительные спецификации<br>- Глоссарий<br>- Документ по архитектуре ПО<br>- План тестирования |
| **Выполнить архитектурное подтверждение концепции (опционально)** | - Архитектор ПО | - Архитектурный анализ<br>- Создать архитектурное подтверждение концепции<br>- Оценить жизнеспособность архитектурного подтверждения концепции | - Документ по архитектуре ПО<br>- Модель анализа<br>- Модель проектирования<br>- Модель развертывания<br>- Архитектурное подтверждение концепции<br>- Запись обзора | Нет |
| **Спланировать проект** | - Руководитель проекта | - Оценить итерацию<br>- Идентифицировать и оценить риски<br>- Спланировать фазы и итерации<br>- Разработать план итерации<br>- Привлечь персонал | - Оценка итерации<br>- Список рисков<br>- План разработки ПО<br>- План итерации | - Список рисков<br>- План разработки ПО<br>- План итерации E1 |

**Веха целей жизненного цикла**

В конце фазы начального замысла проект оценивается по следующим критериям:

- Согласие заинтересованных сторон по определению границ.
- Согласие, что собран правильный набор требований.
- Согласие, что оценки стоимости/сроков, приоритеты, риски и процесс разработки являются приемлемыми.
- Все риски идентифицированы, и для каждого риска существует стратегия снижения.

**Состояние нескольких основных рабочих продуктов на вехе фазы начального замысла:**
- Бизнес-кейс (100% завершено)
- Видение (примерно 100% завершено)
- Глоссарий (примерно 40% завершено)
- План разработки ПО (примерно 80% завершено)
- План итерации для первой итерации проработки (примерно 100% завершено)
- Список рисков (примерно 25% завершено)
- Модель вариантов использования (примерно 20% завершено)
- Дополнительные спецификации (примерно 20% завершено)
- План тестирования (примерно 10% завершено)
- Документ по архитектуре ПО (примерно 10% завершено)
- Архитектурное подтверждение концепции (один или несколько прототипов подтверждения концепции доступны для решения конкретных рисков)

#### 5.2 Основы проработки

Основная цель фазы проработки – зафиксировать базовую линию архитектуры системы, чтобы обеспечить стабильную основу для основной части усилий по проектированию и реализации в фазе построения. Стабильность архитектуры оценивается с помощью одного или нескольких архитектурных прототипов. Фаза проработки состоит из ряда итераций, завершающихся Вехой архитектуры жизненного цикла. Типичная итерация проработки включает виды деятельности, представленные в таблице 5-2 на странице 56. Веха описывается сразу после таблицы.

**Таблица 5-2. Виды деятельности типичной итерации проработки**

| Вид деятельности | Роли | Задачи | Выходные рабочие продукты | Примеры Менеджера каталога |
|---|---|---|---|---|
| **Уточнить требования** | - Спецификатор требований<br>- Системный аналитик<br>- Архитектор ПО | - Детализировать вариант использования<br>- Разработать дополнительные спецификации<br>- Зафиксировать общий словарь<br>- Приоритизировать варианты использования | - Вариант использования<br>- Дополнительные спецификации<br>- Глоссарий<br>- Документ по архитектуре ПО | - Спецификации вариантов использования<br>- Модели UML<br>- Дополнительные спецификации |
| **Определить архитектуру** | - Архитектор ПО<br>- Проектировщик<br>- Технический рецензент | - Архитектурный анализ<br>- Анализ сервисов<br>- Анализ существующих активов<br>- Анализ варианта использования<br>- Идентифицировать элементы проектирования<br>- Описать исполняемую архитектуру<br>- Описать распределение<br>- Провести обзор архитектуры | - Документ по архитектуре ПО<br>- Модель анализа<br>- Модель проектирования<br>- Класс проектирования<br>- Подсистема проектирования<br>- Пакет проектирования<br>- Интерфейс<br>- Модуль<br>- Сигнал<br>- Событие<br>- Модель развертывания<br>- Модель сервисов<br>- Компонент сервиса<br>- Запись обзора | - Документ по архитектуре ПО<br>- Модели UML |
| **Спроектировать компоненты** | - Проектировщик<br>- Архитектор ПО<br>- Проектировщик БД<br>- Проектировщик пользовательского интерфейса<br>- Технический рецензент | - Проектирование варианта использования<br>- Идентифицировать элементы проектирования<br>- Проектирование подсистемы<br>- Проектирование модуля<br>- Проектирование класса<br>- Проектирование подсистемы (SOA)<br>- Спецификация компонента (SOA)<br>- Проектирование БД<br>- Спроектировать пользовательский интерфейс<br>- Создать прототип пользовательского интерфейса<br>- Провести обзор проектирования | - Модель проектирования<br>- Класс проектирования<br>- Подсистема проектирования<br>- Пакет проектирования<br>- Интерфейс<br>- Модуль<br>- Сигнал<br>- Событие<br>- Модель сервисов<br>- Компонент сервиса<br>- Модель данных<br>- Навигационная карта<br>- Прототип пользовательского интерфейса<br>- Запись обзора | - Модели UML |
| **Кодировать и модульно тестировать компоненты** | - Реализатор<br>- Технический рецензент | - Реализовать элементы проектирования<br>- Реализовать тесты разработчика<br>- Выполнить тесты разработчика<br>- Провести обзор кода | - Подсистема реализации<br>- Элемент реализации<br>- Тест разработчика<br>- Журнал тестирования<br>- Запись обзора | Нет |
| **Интегрировать и тестировать** | - Интегратор<br>- Тест-дизайнер<br>- Тест-аналитик<br>- Тестировщик | - Интегрировать подсистему<br>- Интегрировать систему<br>- Определить подход к тестированию<br>- Определить детали тестирования<br>- Реализовать тест<br>- Определить процедуры проверки установки (IVPs)<br>- Реализовать процедуры проверки установки (IVPs)<br>- Выполнить тестовый набор<br>- Проанализировать неудачу теста | - Сборка<br>- Подсистема реализации<br>- Стратегия тестирования<br>- План тестирования<br>- Конфигурация среды тестирования<br>- Тестовый случай<br>- Тестовый сценарий<br>- Журнал тестирования<br>- Процедуры проверки установки (IVPs)<br>- Запрос на изменение | - План тестирования<br>- Тестовые случаи<br>- Процедуры проверки установки (IVPs) |
| **Спланировать проект** | - Руководитель проекта | - Оценить итерацию<br>- Идентифицировать и оценить риски<br>- Спланировать фазы и итерации<br>- Разработать план итерации<br>- Привлечь персонал | - Оценка итерации<br>- Список рисков<br>- План разработки ПО<br>- План итерации | - Список рисков<br>- План разработки ПО |

**Веха архитектуры жизненного цикла**

В конце фазы проработки проект оценивается по следующим критериям:

- Требования к продукту и архитектура стабильны.
- Ключевые подходы, используемые в тестировании и оценке, доказаны.
- Тестирование и оценка исполняемых прототипов продемонстрировали, что основные элементы риска были решены и достоверно устранены.
- Планы итераций для фазы построения достаточно детализированы, чтобы позволить работе продолжаться, и подкреплены достоверными оценками.
- Все заинтересованные стороны согласны, что видение может быть достигнуто, если текущий план будет выполнен для разработки полной системы в контексте текущей архитектуры.
- Фактические затраты ресурсов по сравнению с запланированными являются приемлемыми.

**Состояние нескольких основных рабочих продуктов на вехе фазы проработки:**
- Глоссарий (примерно 80% завершено)
- План разработки ПО (примерно 95% завершено)
- Планы итераций для итераций построения (примерно 100% завершено, по крайней мере для первой итерации)
- Список рисков (примерно 50% завершено)
- Модель вариантов использования (примерно 80% завершено)
- Дополнительные спецификации (примерно 80% завершено)
- Документ по архитектуре ПО (примерно 100% завершено)
- Модель проектирования (примерно 60% завершено)
- Модель сервисов (примерно 60% завершено)
- План тестирования (примерно 30% завершено)
- Тестовые случаи (примерно 40% завершено)
- Тестовые сценарии (примерно 40% завершено)
- Элементы реализации, включая исходный код (примерно 40% завершено)
- Сборки доступны (одна или несколько за итерацию, например)
- Один или несколько исполняемых архитектурных прототипов доступны (для изучения критической функциональности и архитектурно значимых сценариев)
- Процедуры проверки установки (IVPs) (примерно 80% завершено)

#### 5.3 Основы построения

Основная цель фазы построения – завершить разработку системы на основе базовой архитектуры. Фаза построения состоит из ряда итераций, завершающихся Вехой первоначальной операционной готовности. Типичная итерация построения включает виды деятельности, представленные в таблице 5-3. Веха описывается сразу после таблицы.

**Таблица 5-3. Виды деятельности типичной итерации построения**

| Вид деятельности | Роли | Задачи | Выходные рабочие продукты | Примеры Менеджера каталога |
|---|---|---|---|---|
| **Уточнить требования** | - Спецификатор требований<br>- Системный аналитик<br>- Архитектор ПО | - Детализировать вариант использования<br>- Разработать дополнительные спецификации<br>- Зафиксировать общий словарь<br>- Приоритизировать варианты использования | - Вариант использования<br>- Дополнительные спецификации<br>- Глоссарий<br>- Документ по архитектуре ПО | - Спецификации вариантов использования<br>- Модели UML<br>- Дополнительные спецификации |
| **Спроектировать компоненты** | - Проектировщик<br>- Архитектор ПО<br>- Проектировщик БД<br>- Проектировщик пользовательского интерфейса<br>- Технический рецензент | - Проектирование варианта использования<br>- Идентифицировать элементы проектирования<br>- Проектирование подсистемы<br>- Проектирование модуля<br>- Проектирование класса<br>- Проектирование подсистемы (SOA)<br>- Спецификация компонента (SOA)<br>- Проектирование БД<br>- Спроектировать пользовательский интерфейс<br>- Создать прототип пользовательского интерфейса<br>- Провести обзор проектирования | - Модель проектирования<br>- Класс проектирования<br>- Подсистема проектирования<br>- Пакет проектирования<br>- Интерфейс<br>- Модуль<br>- Сигнал<br>- Событие<br>- Модель сервисов<br>- Компонент сервиса<br>- Модель данных<br>- Навигационная карта<br>- Прототип пользовательского интерфейса<br>- Запись обзора | - Модели UML |
| **Кодировать и модульно тестировать компоненты** | - Реализатор<br>- Технический рецензент | - Реализовать элементы проектирования<br>- Реализовать тесты разработчика<br>- Выполнить тесты разработчика<br>- Провести обзор кода | - Подсистема реализации<br>- Элемент реализации<br>- Тест разработчика<br>- Журнал тестирования<br>- Запись обзора | - Исходный код |
| **Интегрировать и тестировать** | - Интегратор<br>- Тест-дизайнер<br>- Тест-аналитик<br>- Тестировщик | - Интегрировать подсистему<br>- Интегрировать систему<br>- Определить подход к тестированию<br>- Определить детали тестирования<br>- Реализовать тест<br>- Определить процедуры проверки установки (IVPs)<br>- Реализовать процедуры проверки установки (IVPs)<br>- Выполнить тестовый набор<br>- Проанализировать неудачу теста | - Сборка<br>- Подсистема реализации<br>- Стратегия тестирования<br>- План тестирования<br>- Конфигурация среды тестирования<br>- Тестовый случай<br>- Тестовый сценарий<br>- Журнал тестирования<br>- Процедуры проверки установки (IVPs)<br>- Запрос на изменение | - План тестирования<br>- Тестовые случаи |
| **Подготовить развертывание** | - Менеджер развертывания<br>- Технический писатель<br>- Реализатор<br>- Разработчик курсов<br>- Графический художник | - Разработать план развертывания<br>- Определить ведомость материалов<br>- Разработать материалы поддержки<br>- Разработать рабочие продукты установки<br>- Разработать учебные материалы<br>- Создать художественное оформление продукта | - План развертывания<br>- Ведомость материалов<br>- Материалы поддержки пользователей<br>- Артефакты установки<br>- Учебные материалы<br>- Художественное оформление продукта | Нет |
| **Спланировать проект** | - Руководитель проекта | - Оценить итерацию<br>- Идентифицировать и оценить риски<br>- Спланировать фазы и итерации<br>- Разработать план итерации<br>- Привлечь персонал | - Оценка итерации<br>- Список рисков<br>- План разработки ПО<br>- План итерации | - Список рисков<br>- План разработки ПО |

**Веха первоначальной операционной готовности**

Критерии оценки для фазы построения включают ответы на эти вопросы:

- Достаточно ли стабилен и зрел этот релиз продукта для развертывания в пользовательском сообществе?
- Готовы ли все заинтересованные стороны к переходу в пользовательское сообщество?
- Приемлемы ли фактические затраты ресурсов по сравнению с запланированными затратами ресурсов?

**Состояние нескольких основных рабочих продуктов на вехе фазы построения:**
- Глоссарий (примерно 100% завершено)
- План разработки ПО (примерно 100% завершено)
- Планы итераций для итераций перехода (примерно 100% завершено, по крайней мере для первой итерации)
- Список рисков (примерно 75% завершено)
- Модель вариантов использования (примерно 100% завершено)
- Дополнительные спецификации (примерно 100% завершено)
- Модель проектирования (примерно 100% завершено)
- Модель сервисов (примерно 100% завершено)
- План тестирования (примерно 90% завершено)
- Тестовые случаи (примерно 80% завершено)
- Тестовые сценарии (примерно 80% завершено)
- Элементы реализации, включая исходный код (примерно 90% завершено)
- Сборки доступны (одна или несколько за итерацию, например)
- Исполняемая система доступна
- Процедуры проверки установки (IVPs) (примерно 90% завершено)
- Материалы поддержки пользователей (примерно 40% завершено)

#### 5.4 Основы перехода

Основная цель фазы перехода – обеспечить доступность программного обеспечения для пользователей. Она включает тестирование продукта в рамках подготовки к выпуску, внесение незначительных корректировок на основе отзывов пользователей и фокусировку в основном на тонкой настройке продукта, конфигурации, установке и проблемах удобства использования. Фаза перехода состоит из ряда итераций, завершающихся Вехой выпуска продукта. Типичная итерация перехода включает виды деятельности, представленные в таблице 5-4. Веха описывается сразу после таблицы.

**Таблица 5-4. Виды деятельности типичной итерации перехода**

| Вид деятельности | Роли | Задачи | Выходные рабочие продукты | Примеры Менеджера каталога |
|---|---|---|---|---|
| **Кодировать и модульно тестировать компоненты** | - Реализатор<br>- Технический рецензент | - Реализовать элементы проектирования<br>- Реализовать тесты разработчика<br>- Выполнить тесты разработчика<br>- Провести обзор кода | - Подсистема реализации<br>- Элемент реализации<br>- Тест разработчика<br>- Журнал тестирования<br>- Запись обзора | - Исходный код |
| **Интегрировать и тестировать** | - Интегратор<br>- Тест-дизайнер<br>- Тест-аналитик<br>- Тестировщик | - Интегрировать подсистему<br>- Интегрировать систему<br>- Определить подход к тестированию<br>- Определить детали тестирования<br>- Реализовать тест<br>- Определить процедуры проверки установки (IVPs)<br>- Реализовать процедуры проверки установки (IVPs)<br>- Выполнить тестовый набор<br>- Проанализировать неудачу теста | - Сборка<br>- Подсистема реализации<br>- Стратегия тестирования<br>- План тестирования<br>- Конфигурация среды тестирования<br>- Тестовый случай<br>- Тестовый сценарий<br>- Журнал тестирования<br>- Процедуры проверки установки (IVPs)<br>- Запрос на изменение | - План тестирования<br>- Тестовые случаи<br>- Процедуры проверки установки (IVPs) |
| **Выполнить бета- и приемочное тестирование** | - Менеджер развертывания<br>- Руководитель проекта<br>- Тестировщик | - Разработать план приемки продукта<br>- Выполнить тестовый набор<br>- Проанализировать неудачу теста<br>- Управлять бета-тестированием<br>- Управлять приемочным тестированием | - План приемки продукта<br>- Журнал тестирования<br>- Запрос на изменение | Нет |
| **Упаковать продукт** | - Менеджер развертывания<br>- Технический писатель<br>- Реализатор<br>- Разработчик курсов<br>- Графический художник<br>- Менеджер конфигурации | - Написать примечания к выпуску<br>- Определить ведомость материалов<br>- Разработать материалы поддержки<br>- Разработать рабочие продукты установки<br>- Разработать учебные материалы<br>- Создать художественное оформление продукта<br>- Создать единицу развертывания<br>- Выпустить в производство<br>- Проверить произведенный продукт<br>- Обеспечить доступ к сайту загрузки | - Примечания к выпуску<br>- Ведомость материалов<br>- Материалы поддержки пользователей<br>- Артефакты установки<br>- Учебные материалы<br>- Художественное оформление продукта<br>- Единица развертывания<br>- Продукт | Нет |
| **Спланировать проект** | - Руководитель проекта<br>- Рецензент руководства | - Оценить итерацию<br>- Идентифицировать и оценить риски<br>- Спланировать фазы и итерации<br>- Разработать план итерации<br>- Привлечь персонал<br>- Подготовить к закрытию проекта<br>- Провести обзор приемки проекта | - Оценка итерации<br>- Список рисков<br>- План разработки ПО<br>- План итерации<br>- Список проблем<br>- Оценка статуса<br>- Запись обзора | - Список рисков |

**Веха выпуска продукта**

Основные критерии оценки фазы перехода включают ответы на эти вопросы:

- Удовлетворен ли пользователь?
- Приемлемы ли фактические затраты ресурсов по сравнению с запланированными?

На вехе выпуска продукта продукт находится в производстве, и начинается цикл поддержки после выпуска.

**Сводка нескольких основных рабочих продуктов, завершенных на вехе фазы перехода:**
- Список рисков
- План тестирования
- Тестовые случаи
- Тестовые сценарии
- Элементы реализации, включая исходный код
- Единица развертывания
- Сборка
- Материалы поддержки пользователей
- Процедуры проверки установки (IVPs)
- Продукт

### 6. Сквозной жизненный цикл

IBM Rational Unified Process для System z (RUP для System z) включает процесс поставки, который охватывает весь жизненный цикл разработки от начала до конца. Этот процесс поставки может использоваться в качестве шаблона для планирования и выполнения проекта. Он предоставляет полную модель жизненного цикла с предопределенными фазами, итерациями, видами деятельности и задачами. Он включает структуру декомпозиции работ (СДР).

Процесс поставки RUP для System z доступен на веб-сайте RUP для System z, как показано на рисунке 6-1 на странице 66.

### 7. Элементы содержания

IBM Rational Unified Process для System z (RUP для System z) включает большое количество элементов содержания (роли, задачи и артефакты), которые составляют ядро метода. Большинство этих элементов взяты из Rational Unified Process (RUP) и его расширения для сервисно-ориентированной архитектуры (SOA). Однако несколько элементов содержания были добавлены в RUP для System z, потому что они специфичны для среды System z. В этой главе представлены эти новые элементы содержания.

#### 7.1 Артефакт: Модуль

Модуль – это элемент программного обеспечения, который группирует связный набор подпрограмм, процедур и структур данных. Модули – это отдельные повторно используемые единицы программного обеспечения, которые могут создаваться, редактироваться и компилироваться отдельно и одновременно. Модули также способствуют модульности и инкапсуляции (т.е. сокрытию информации), что облегчает понимание сложных программ.

Модули обеспечивают разделение между спецификацией, реализацией и исполнением. Спецификация модуля выражает элементы, предоставляемые и требуемые реализацией модуля, а затем исполнением. Элементы, определенные во время спецификации для интерфейса, видимы другим модулям. Исполнение содержит рабочий код, соответствующий элементам, объявленным в спецификации и реализации.

В объектно-ориентированном мире мы говорим о классах. Классы – это категория объектов. Класс определяет общие свойства и общее поведение различных объектов, которые принадлежат ему. Другими словами, класс – это описание набора объектов, которые разделяют одни и те же атрибуты, операции, методы, отношения и семантику. Обычно в UML у вас есть собственное представление для классов (элемент класса), и вы можете специфицировать их, предоставляя такую информацию, как имя, атрибуты, методы, отношения и некоторые другие общие описания. Поскольку многие из этих спецификаций являются общими между классами и модулями и поскольку класс также может быть описан через исходный код модуля (например, MyClass.java), вы можете использовать элемент класса UML для моделирования ваших модулей. Однако вам нужно быть осторожным в отношении их различий.

**Различия между классами и модулями:**
- Классы могут наследовать свойства и поведение от другого класса.
- Классы создают экземпляры для создания объектов.
- Полиморфизм позволяет динамические отношения (экземпляры классов могут меняться во время выполнения), в то время как отношения между модулями статичны.

**Сходства между классами и модулями:**
- Модули и классы могут образовывать иерархию.
- Модули и классы могут использовать инкапсуляцию для сокрытия деталей реализации.

Таким образом, как описано выше, вы можете представить модуль через элемент класса UML, но чтобы избежать недопонимания между классами и модулями, вы также должны предоставить конкретные инструкции для заинтересованного лица, которому нужно читать вашу модель. Предлагаемый подход – использовать технику стереотипов, которая позволяет вам расширять язык UML, предоставляя необходимые инструкции для читателей; например, вы можете использовать стереотип `<<Module>>`, чтобы указать, что элемент модели на вашей диаграмме представляет модуль, а не класс.

#### 7.2 Задача: Проектирование модуля

Эта задача определяет, как спроектировать модульную структуру подсистемы или компонента.

**Цель:**
- Обеспечить, чтобы модуль обеспечивал поведение, требуемое реализациями вариантов использования.
- Обеспечить, чтобы была предоставлена достаточная информация для однозначной реализации модуля.
- Обработать нефункциональные требования, связанные с модулем.
- Включить механизмы проектирования, используемые модулем.

**Основное описание:**
Поскольку большинство систем, даже небольших, должны быть спроектированы перед реализацией, чтобы избежать дорогостоящей переделки из-за ошибок проектирования, задача проектирования модуля определяет элементы проектирования программных модулей, необходимые для обеспечения правильного поведения реализаций вариантов использования, чтобы модули точно выполняли предполагаемую работу системы, подсистемы или компонента. Другие элементы проектирования, такие как подсистемы, пакеты и совместные работы, описывают, как модули сгруппированы вместе или как они взаимодействуют.

**Шаги:**
1. **Решить, генерировать ли код:** Способ проектирования отличается в зависимости от того, генерируется ли код из модели проектирования или нет. Если код генерируется, проектирование должно быть очень детальным и должно синхронизироваться с кодом. С другой стороны, если код не генерируется, то нет необходимости в детальной модели проектирования.
2. **Использовать шаблоны проектирования и механизмы:** Шаблон проектирования – это повторяемое решение для повторяющейся проблемы в проектировании программного обеспечения. Использование шаблонов проектирования и механизмов может быть большим преимуществом в проектировании классов, модулей или возможностей.
3. **Обеспечить соответствующее использование определений UML:** Чтобы лучше понять элементы модели, используемые в диаграммах модели проектирования, нам нужно расширить язык UML для лучшей поддержки концепции модуля за пределами встроенного определения класса. Например, вы можете рассмотреть использование простых стереотипов или полностью детализированных профилей UML.
4. **Создать один или несколько начальных модулей проектирования для артефакта: Элементы анализа, заданные в качестве входных данных для этой задачи, и назначить зависимости трассировки.** Модули проектирования – это представления программных модулей в общей модели проектирования.
5. **Идентифицировать постоянные модули:** Элементы анализа, которым необходимо хранить свое состояние на постоянном носителе, называются постоянными. Включить механизмы проектирования, соответствующие механизмам постоянства, найденным во время анализа.
6. **Определить операции:** Для идентификации операций в модулях проектирования изучить обязанности каждого соответствующего класса анализа, создавая операцию для каждой обязанности. Изучить реализации вариантов использования в представлении участвующих классов, чтобы увидеть, как операции используются реализациями вариантов использования.
7. **Определить атрибуты:** Во время определения операций идентифицируются атрибуты, необходимые модулю для выполнения своих операций. Для каждого атрибута определить его имя, тип, значение по умолчанию или начальное значение, видимость и постоянство данных.
8. **Определить зависимости:** Для каждого случая, когда требуется общение между модулями, установить зависимость между модулями на диаграмме классов, содержащей два модуля.
9. **Оценить ваши результаты:** Проверить модель проектирования на этом этапе, чтобы убедиться, что ваша работа движется в правильном направлении.

#### 7.3 Артефакт: Процедуры проверки установки (IVPs)

Этот рабочий продукт – это одна или несколько программ или сценариев (ручных или автоматизированных), которые запускаются в конце установки программного приложения.

**Цель:**
Цель IVPs – проверить, что установленная программа или приложение функционирует правильно в среде, в которой она установлена.

**Основное описание:**
Рекомендуется использовать IVP, особенно в сложной программе или приложении, которые могут работать в различных средах. В случае простого приложения может быть достаточно просто выполнения функций приложения.

#### 7.4 Задача: Определить процедуры проверки установки (IVPs)

Эта задача определяет IVPs, которые будут запускаться в конце установки программного приложения.

**Цель:**
Цель этой задачи – идентифицировать требования к среде установки и спроектировать IVPs, необходимые для проверки того, что установленная программа или приложение функционирует правильно в среде, в которой она установлена.

**Шаги:**
1. **Идентифицировать требования к среде установки:** Определить основные элементы, которые должны быть на месте, чтобы обеспечить успешный запуск установленной программы.
2. **Определить IVPs, которые выполняют основные функции:** Определить IVPs, которые выполняют основные функции, которые должны быть поставлены.
3. **Определить IVPs, которые проверяют ключевые аспекты пользовательского интерфейса:** Если программа или приложение в основном интерактивно управляемое, а не пакетное, вы можете определить IVP, который проверяет ключевой пользовательский интерфейс.

#### 7.5 Задача: Реализовать процедуры проверки установки (IVPs)

Эта задача реализует IVPs, которые будут проверять, что установленная программа или приложение функционирует правильно в среде, в которой она установлена.

**Цель:**
Цель этой задачи – реализовать IVPs, необходимые для проверки того, что установленная программа или приложение функционирует правильно в среде, в которой она установлена. Реализация IVP означает предоставление исполняемого кода или сценария для IVP или предоставление подробных инструкций, описывающих, как вручную выполнить IVP.

**Шаги:**
1. **Реализовать автоматизированные IVPs:** Предоставить исполняемый код или сценарий для каждого IVP.
2. **Реализовать ручные IVPs:** Предоставить подробные инструкции, описывающие, как вручную выполнить каждый IVP.
3. **Объединить IVPs в тестовый набор:** Упаковать IVPs в тестовый набор, чтобы их можно было выполнять отдельно от других типов тестов.

#### 7.6 Артефакт: Элемент анализа

Виды деятельности RUP по анализу и проектированию начинаются с идентификации концептуальных классов, которые называются классами анализа. Классы анализа специфицируют ранние концептуальные "вещи" в системе, которые имеют обязанности и поведение. Позже они уточняются в детальные классы проектирования или другие элементы проектирования. Чтобы обобщить этот подход на не объектно-ориентированные среды разработки в RUP для System z, класс анализа переименован в элемент анализа, так что элемент анализа может использоваться для идентификации концептуальных вещей, которые позже могут быть превращены в модули, классы или любой другой элемент проектирования.

**Цель:**
Элементы анализа используются для захвата основных "сгустков ответственности" в системе.

**Основное описание:**
Элементы анализа специфицируют элементы ранней концептуальной модели для вещей в системе, которые имеют обязанности и поведение. Они представляют прототипические элементы системы и являются "первым проходом" по основным абстракциям, с которыми система должна работать. Элементы анализа могут поддерживаться сами по себе, если желателен "высокоуровневый", концептуальный обзор системы. Элементы анализа также дают начало основным абстракциям проектирования системы.

#### 7.7 Задача: Анализ сервисов

Эта задача идентифицирует элементы проектирования сервисно-ориентированного решения с точки зрения сервисов и разделов и документирует начальную спецификацию этих сервисов.

**Цель:**
- Идентифицировать элементы проектирования сервисно-ориентированного решения с точки зрения сервисов и разделов.
- Документировать начальную спецификацию сервисов.
- Определить начальные зависимости и общение между сервисами.

**Основное описание:**
Анализ сервисов – это процесс идентификации и проверки кандидатов в сервисы, компоненты и потоки. Эти кандидаты в сервисы могут потребовать дополнительного уточнения; однако шаги, включенные здесь, предоставляют эффективный способ создания начального набора артефакта: Спецификация сервиса.

**Шаги:**
1. **Принять подход к идентификации сервисов:** Выбрать подход к идентификации сервисов из ряда доступных подходов, чтобы поддержать вас в идентификации сервисов, которые будут частью создаваемого вами решения.
2. **Идентифицировать разделы сервисов:** Специфицировать набор логических разделов, которые будут использоваться для организации сервисов, которые будут частью создаваемого вами решения.
3. **Анализировать существующие активы:** Существующие системы, такие как пакетные или пользовательские приложения, а также отраслевые стандарты, модели и активы, являются основным источником для использования при выполнении реализации сервисов.
4. **Идентифицировать сервисы:** Специфицировать кандидатов в сервисы, которые будут использоваться в решении.
5. **Разработать начальную спецификацию сервиса:** Специфицировать композицию и совместную работу кандидатов в сервисы, составляющих решение.

### 8. Тематическое исследование "Менеджер каталога"

Цель этой главы – применить знания, полученные из предыдущих глав этой публикации IBM Redbooks, и использовать их для разработки примера приложения.

Эта глава предоставляет справочный материал, чтобы помочь практикам в разработке приложения итеративно в среде System z. Определяя сходства между тематическим исследованием и упражнением по разработке в вашей среде, вы можете использовать эту главу в качестве руководства для оценки временных интервалов, идентификации задействованных задач и лучшего понимания методологии разработки на конкретном примере.

В тематическом исследовании используется приложение "Менеджер каталога" CICS для предоставления примера реализации Rational Unified Process для System z (RUP для System z). Это рабочее приложение COBOL, которое поставляется с CICS TS 3.1 и предназначено для иллюстрации лучших практик по представлению приложений CICS как веб-сервисов.

#### 8.1 Обзор приложения "Менеджер каталога"

Приложение "Менеджер каталога" – это приложение для управления каталогом, стиля заказа на покупку, которое обращается к каталогу заказов, хранящемуся в файле VSAM.

Оно предоставляет следующие функции:
- Показать детали элемента в каталоге.
- Заказать количество определенного элемента.
- Пополнить элементы в каталоге, которые были исчерпаны.

После того как элемент заказан, каталог автоматически обновляется, чтобы отразить новые уровни запасов. Пополненные элементы в каталоге сбрасываются до количества запаса 100.

Приложение доступно как через интерфейс терминала 3270, так и через веб-интерфейс с использованием коммерчески доступного интернет-браузера. SOAP и веб-сервисы используются для представления контролируемой CICS информации (функций менеджера каталога) в качестве поставщиков услуг сервисно-ориентированной архитектуры (SOA), которые, в свою очередь, доступны с использованием запросчиков услуг SOA из браузера.

#### 8.2 Итерационный процесс разработки "Менеджера каталога"

Применяя итерационный процесс к нашему тематическому исследованию, график разработки "Менеджера каталога" разделен на восемь итераций, каждая итерация длится три недели. Итерационный цикл, как обсуждается в главе 3, обычно длится от двух до трех недель, с общим количеством итераций, распределенных среди четырех фаз RUP: Начальный замысел, Проработка, Построение и Переход. Итерационный цикл – это сердцебиение проекта, и после того, как он выбран, он остается постоянным на протяжении всего проекта. Как цикл итерации, так и количество итераций зависят от проекта, причем последнее напрямую связано со сложностью проекта.

План итерационной разработки "Менеджера каталога" включает одну итерацию в фазе начального замысла, три итерации в фазе проработки, две итерации в фазе построения и две итерации в фазе перехода. Мы оцениваем и снижаем риски во время каждой итерации, причем каждая итерация завершается второстепенной вехой для проекта и способствует успешному достижению целей фазы.

#### 8.3 Фазы RUP "Менеджера каталога"

Виды деятельности в каждой фазе в первую очередь сосредоточены на решении определенного набора рисков с целью снижения рисков и обеспечения продвижения проекта вперед. Вехи в конце каждой фазы служат двойному процессу:

- Веха служит движущей силой для достижения конкретной цели, предоставляя статус разработки нашим заинтересованным сторонам, чьи решения являются ключевыми для перехода к следующей фазе.
- Вехи являются контрольными точками для проекта в целом, поскольку они позволяют разработчикам и руководству отслеживать прогресс работы по мере завершения ключевых точек в жизненном цикле проекта.

##### 8.3.1 Фаза начального замысла "Менеджера каталога"

Фаза начального замысла решает бизнес-риски, чтобы мы сосредоточились на снижении риска, что проект может быть либо экономически нецелесообразным, либо технически неосуществимым. Во время этой фазы крайне важно обсудить с заинтересованными сторонами их потребности и проблемы, которые наше решение пытается решить. Мы тщательно изучаем все аспекты проекта, а также определяем основные варианты использования.

Один из рисков, идентифицированных при создании приложения "Менеджер каталога", – это незнакомство команды разработки программного обеспечения с архитектурой и технологией веб-сервисов, что может помешать им своевременно поставить компонент веб-сервисов. Чтобы снизить этот риск, мы решаем предоставить раннее обучение по веб-сервисам членам команды в первой итерации фазы проработки, до разработки компонента веб-сервисов.

Определение основных вариантов использования для системы заказа каталога, такой как "Менеджер каталога", включает получение согласия всех, что клиенту необходимо иметь возможность просматривать элементы в каталоге, а также заказывать определенное количество конкретного элемента. Кроме того, представитель службы поддержки клиентов должен иметь возможность пополнять (восстанавливать запасы) исчерпанные элементы в каталоге.

**Завершение фазы начального замысла:**
Фаза начального замысла для "Менеджера каталога" завершается Вехой целей жизненного цикла, которая указывает, продолжать или отказываться от проекта. На этом этапе мы предлагаем единое решение, которое:
- Решает правильную проблему.
- Технически осуществимо.
- Экономически жизнеспособно.

Все заинтересованные стороны согласны с этими пунктами до перехода проекта к следующему шагу, то есть разработке архитектурного подхода в фазе проработки. Если все заинтересованные стороны не согласны с этими пунктами, принимается решение об отмене проекта. Это на самом деле может быть желаемым результатом фазы начального замысла, поскольку прекращение проекта на этом этапе является наименее затратным вариантом из всех фаз.

**Итерации в фазе начального замысла:**
Фаза начального замысла имеет только одну итерацию.

**Рабочие продукты, произведенные в фазе начального замысла:**
- Бизнес-кейс (100%)
- Видение (100%)
- Глоссарий (40%)
- План разработки ПО (80%)
- Список рисков (25%)
- Модель вариантов использования (20%)
- Дополнительные спецификации (20%)
- Документ по архитектуре ПО (10%)
- План тестирования "Менеджера каталога" (10%)
- План итерации E1 (100%)

**Инструменты, используемые в фазе начального замысла:**
- IBM Rational Software Architect/Modeler
- IBM Rational SoDA
- IBM Rational RequisitePro
- IBM Rational Method Composer и IBM Rational Portfolio Manager
- IBM Rational Clear Case

##### 8.3.2 Фаза проработки "Менеджера каталога"

Фаза проработки решает архитектурные и технические риски. Она охватывает три итерации, завершающиеся Вехой архитектуры жизненного цикла, которая представляет собой исполняемую архитектуру. Это частичная реализация системы для проверки того, что у нас есть стабильная архитектура для поддержки значительных требований Функциональности, Удобства использования, Надежности, Производительности и Масштабируемости (FURPS).

Во время этой фазы мы описываем основные и альтернативные потоки каждого варианта использования, а также определяем наиболее критичные (важные) варианты использования. Для каждого критического варианта использования мы определяем архитектурно значимые (наиболее важные) сценарии для "Менеджера каталога" и используем их для создания исполняемой архитектуры; то есть мы проектируем, реализуем и тестируем эти сценарии. Мы также документируем эти архитектурные сценарии в нашем Документе по архитектуре программного обеспечения.

**Итерации в фазе проработки:**
Фаза проработки имеет три итерации: E1, E2 и E3.

- **Итерация E1:** Сфокусирована на реализации архитектурного прототипа для компонента CICS приложения "Менеджер каталога". Реализует вариант использования "Показать элементы каталога" для интерфейса 3270.
- **Итерация E2:** Сфокусирована на реализации архитектурного прототипа для компонента веб-сервисов "Менеджера каталога". Реализует вариант использования "Настроить каталог" для веб-сервисов.
- **Итерация E3:** Сфокусирована на завершении анализа и проектирования для всех оставшихся высокорисковых требований, связанных с веб-сервисами. Реализует вариант использования "Показать элементы каталога" как веб-сервис.

**Завершение фазы проработки:**
Фаза проработки для "Менеджера каталога" завершается Вехой архитектуры жизненного цикла. Наша цель на этом этапе:
- Взять под контроль архитектурные и технические риски.
- Установить и продемонстрировать прочный архитектурный фундамент.
- Установить достоверный план для разработки продукта.

Решение о переходе к фазе построения принимается на основе того, что мы снизили технические риски, которые мы определили.

**Рабочие продукты, произведенные в фазе проработки:**
- Глоссарий (80%)
- План разработки ПО (95%)
- Планы итераций E2, E3 и C1 (100%)
- План итерации C2 (80%)
- Список рисков (50%)
- Модель вариантов использования, включая спецификации вариантов использования (80%)
- Дополнительные спецификации (80%)
- Документ по архитектуре ПО (100%)
- Модель анализа (50%)
- Модель проектирования (60%)
- Модель сервисов (60%)
- План тестирования (30%)
- Тестовые случаи, включая тестовые сценарии (40%)
- Сводка оценки тестирования (Создана)
- Исходный код (40%)
- Сборки для E1, E2 и E3 (Созданы)
- Процедуры проверки установки (IVPs) (80%)

**Инструменты, используемые в фазе проработки:**
- IBM Rational Software Architect/Modeler
- IBM Rational SoDA
- IBM Rational RequisitePro
- IBM WebSphere Developer for zSeries (WDz)
- IBM Rational Portfolio Manager
- IBM Rational Clear Case

##### 8.3.3 Фаза построения "Менеджера каталога"

Фаза построения решает логистические риски, то есть завершение оставшейся работы в отведенное время. Она охватывает две итерации, завершающиеся Вехой первоначальной операционной готовности, которая оценивает, подходит ли продукт для поставки пользователям.

Во время этой фазы мы выполняем большую часть работы и реализуем всю функциональность. Оставшиеся сценарии детализируются, проектируются, реализуются и тестируются, следуя шаблону, не unlike таковому в фазе проработки.

**Итерации в фазе построения:**
Фаза построения имеет две итерации: C1 и C2.

- **Итерация C1:** Сфокусирована на реализации варианта использования "Заказать элемент" как для интерфейса 3270, так и для веб-клиентского интерфейса.
- **Итерация C2:** Сфокусирована на реализации варианта использования "Пополнить запасы" как для интерфейса 3270, так и для веб-клиентского интерфейса, а также на подготовке бета-релиза.

**Завершение фазы построения:**
Фаза построения для "Менеджера каталога" завершается Вехой первоначальной операционной готовности. Наша цель на этом этапе:
- Обеспечить, чтобы решение было разработано в соответствии с требованиями.
- Обеспечить, чтобы решение было готово к поставке пользователям и заинтересованным сторонам.
- Достичь адекватного качества как можно быстрее.

Теперь мы готовы развернуть решение как бета-релиз для оценки пользователями и заинтересованными сторонами. Это приводит нас к фазе перехода.

**Рабочие продукты, произведенные в фазе построения:**
- Глоссарий (90%)
- План разработки ПО (100%)
- Планы итераций C2 и T1 (100%)
- План итерации T2 (80%)
- Список рисков (75%)
- Модель вариантов использования, включая спецификации вариантов использования (100%)
- Дополнительные спецификации (100%)
- Модель анализа (100%)
- Модель проектирования (95%)
- Модель сервисов (95%)
- План тестирования (90%)
- Тестовые случаи, включая тестовые сценарии (80%)
- План развертывания (Создан)
- Исходный код (95%)
- Сборки для C1, C2 и Beta (Созданы)
- Процедуры проверки установки (IVPs) (90%)

**Инструменты, используемые в фазе построения:**
- IBM Rational Software Architect/Modeler
- IBM Rational SoDA
- IBM Rational RequisitePro
- IBM WebSphere Developer for zSeries (WDz)
- IBM Rational Manual Tester
- IBM Rational Functional Tester
- IBM Rational Portfolio Manager
- IBM Rational Clear Case

##### 8.3.4 Фаза перехода "Менеджера каталога"

Фаза перехода решает риски внедрения (поставки) решения и берет эти риски под контроль. Она охватывает две итерации, завершающиеся Вехой выпуска продукта, которая отмечает завершение продукта. Во время этой фазы мы в основном озабочены развертыванием и исправлением дефектов, выявленных в выпущенном продукте. Мы решаем поставить "Менеджер каталога" в виде двух релизов: R1, содержащий только компоненты 3270, и R2, содержащий компоненты веб-сервисов.

**Итерации в фазе перехода:**
Фаза перехода имеет две итерации: T1 и T2.

- **Итерация T1:** Сфокусирована на развертывании бета-релиза и исправлении связанных дефектов. После устранения этих дефектов и удовлетворения наших пользователей и заинтересованных сторон мы упаковываем и развертываем R1 продукта, который содержит только компоненты 3270.
- **Итерация T2:** Сфокусирована на развертывании второго релиза, R2, который содержит только компоненты веб-сервисов. Мы обеспечиваем предоставление достаточного количества учебных материалов, поскольку этот релиз более комплексный.

**Завершение фазы перехода:**
Фаза перехода для "Менеджера каталога" завершается Вехой выпуска продукта. Наша цель на этом этапе:
- Поставить решение пользователям.
- Достичь самостоятельности пользователей.

Успешное развертывание продукта указывает на то, что Веха выпуска продукта была достигнута. Оценка вехи выпуска продукта, конечно, основана на удовлетворенности наших пользователей и заинтересованных сторон.

**Рабочие продукты, произведенные в фазе перехода:**
- Глоссарий (100%)
- Планы итераций T2 (100%)
- Список рисков (100%)
- Модель проектирования (100%)
- Модель сервисов (100%)
- План тестирования (100%)
- Тестовые случаи (100%)
- Тестовые сценарии (100%)
- Исходный код (элементы реализации) (100%)
- Процедуры проверки установки (IVPs) (100%)
- Сборки для R1 и R2 (Созданы)

**Инструменты, используемые в фазе перехода:**
- IBM Rational Software Architect/Modeler
- IBM Rational Manual Tester
- IBM Rational Functional Tester
- IBM Rational Portfolio Manager
- IBM Rational Clear Case

### 9. Тематическое исследование по использованию веб-сервисов EGL

Цель этой главы – предоставить введение в язык Enterprise Generation Language (EGL) и проиллюстрировать, как быстро и просто его можно использовать для разработки веб-интерфейса тематического исследования приложения "Менеджер каталога", представленного в предыдущей главе.

#### 9.1 Введение в Enterprise Generation Language

Enterprise Generation Language (EGL) – это высокопроизводительный и интуитивно понятный язык программирования высокого уровня, который позволяет разработчику сосредоточиться на бизнес-логике, а не на нюансах среды выполнения целевой платформы. Например, разработчик System z может быстро разработать веб-клиент без обширных знаний программирования промежуточного слоя или JAVA/J2EE™. Исходный код EGL генерируется либо в COBOL, либо в Java в зависимости от желаемой целевой среды выполнения. Один и тот же исходный код может быть развернут на различных платформах выполнения. Спецификации целевой среды ограничены файлами дескрипторов сборки, которые контролируют процесс генерации. Файлы дескрипторов сборки и определения записей также изолируют специфику хранилищ данных, позволяя разработчику EGL использовать упрощенные конструкции кодирования для доступа к данным независимо от нижележащего хранилища данных, такого как реляционная база данных, база данных DL/I, MQ Series и последовательный файл.

#### 9.2 Подход к разработке

Тематическое исследование "Менеджера каталога" включало использование EGL для разработки веб-интерфейса для запроса веб-сервисов CICS. Предыдущая глава концентрируется на применении разработки RUP для Z во время тематического исследования. Эта глава подчеркивает построение кода.

#### 9.3 Фаза начального замысла

В соответствии с планом разработки программного обеспечения "Менеджера каталога" в фазе начального замысла не происходило никаких специфических для EGL видов деятельности.

#### 9.4 Фаза проработки

Этот раздел дает подробный отчет о том, как воссоздать исполняемую архитектуру, разработанную во время фазы проработки. Основные виды деятельности – это вызов веб-сервиса, кэширование данных сеанса и форматирование данных.

##### 9.4.1 Вызов веб-сервиса

Описываются шаги по созданию веб-проекта EGL, импорту WSDL-файла, тестированию WSDL-файла, генерации артефактов EGL из WSDL-файла, созданию JSP-страницы, настройке обработчика страниц EGL, запуску сервера и тестированию страницы.

##### 9.4.2 Обработка ошибок

Рассматривается создание простых JSP-страниц для отображения ошибок приложения и деталей системных исключений, а также модификация функций вызова веб-сервисов для обработки исключений и навигации между страницами.

##### 9.4.3 Прототип настройки приложения

Описаны шаги по созданию страницы настройки приложения, которая позволяет пользователю задавать конечные точки веб-сервисов и кэшировать их в объекте сеанса.

##### 9.4.4 Форматирование данных

Рассматривается использование записей EGL для улучшения форматирования данных, отображаемых на веб-странице, включая улучшение меток столбцов, форматирование денежных значений, выравнивание числовых значений и отображение нулей вместо пробелов.

#### 9.5 Фаза построения

В фазе построения разработчики EGL включили результаты фазы проработки веб-разработчиков. Веб-разработчики определили внешний вид, навигацию приложения, указав шаблон страницы, таблицы стилей и графику.

##### 9.5.1 Простые страницы ответов

Рассматривается создание простых страниц ответов, таких как приветственная страница, страница деталей ошибки приложения, страница деталей системного исключения, страница ответа на заказ и страница ответа на пополнение запасов, с использованием шаблона страницы.

##### 9.5.2 Страницы запросов веб-сервисов

Описано создание страниц, которые запрашивают веб-сервис и отображают либо страницу ошибки, либо простую страницу ответа в зависимости от результатов. Для повышения производительности определяется шаблон EGL для сокращения процесса кодирования вызова веб-сервиса. Рассматривается создание страниц для размещения заказа, пополнения запасов, запроса одного элемента и запроса каталога.

##### 9.5.3 Страницы с интенсивным использованием HTML

Описано создание страницы ответа на запрос, которая отображает таблицу данных с возможностью выбора элемента для размещения заказа, и страницы настройки приложения, которая позволяет пользователю задавать конечные точки для различных веб-сервисов.

##### 9.5.4 Тестовый сценарий

Представлен пошаговый тестовый сценарий для проверки функциональности приложения, включая настройку конечных точек веб-сервисов, запрос каталога, размещение заказа, запрос одного элемента и пополнение запасов, а также тестирование обработки ошибок при неверных конечных точках.

#### 9.6 Фаза перехода

В соответствии с планом разработки программного обеспечения "Менеджера каталога" в фазе перехода не происходило никаких специфических для EGL видов деятельности.

#### 9.7 Резюме

Эта глава представляет собой пошаговое руководство, которое поможет вам воссоздать часть EGL примера приложения RUP для z "Менеджер каталога". Если вы проработаете эту главу, вы обнаружите, как EGL позволяет очень быстро разрабатывать веб-приложение.

### 10. Структура декомпозиции работ (СДР) IBM RUP для System z

IBM Rational Unified Process для System z (RUP для System z) включает структуру декомпозиции работ, которая охватывает весь жизненный цикл разработки от начала до конца, как показано на рисунке 10-1. Эта структура декомпозиции работ может использоваться в качестве шаблона для планирования и выполнения проекта. В этой главе представлена структура декомпозиции работ для каждой фазы проекта (начальный замысел, проработка, построение и переход).

#### 10.1 Фаза начального замысла

На рисунке 10-2 представлена структура декомпозиции работ для типичной итерации в начальном замысле. Эта структура декомпозиции работ включает виды деятельности и задачи с предшественниками. Количество шагов на задачу показано синими точками.

#### 10.2 Фаза проработки

На рисунке 10-3 представлена структура декомпозиции работ для типичной итерации в проработке. Эта структура декомпозиции работ включает виды деятельности и задачи с предшественниками. Количество шагов на задачу показано синими точками.

#### 10.3 Фаза построения

На рисунке 10-4 представлена структура декомпозиции работ для типичной итерации в построении. Эта структура декомпозиции работ включает виды деятельности и задачи с предшественниками. Количество шагов на задачу показано синими точками.

#### 10.4 Фаза перехода

На рисунке 10-5 представлена структура декомпозиции работ для типичной итерации в переходе. Эта структура декомпозиции работ включает виды деятельности и задачи с предшественниками. Количество шагов на задачу показано синими точками.

### 11. Как настроить IBM Rational Unified Process для System z

Одна из самых распространенных потребностей, связанных с реализацией процесса, – это его настройка. Обычно людям не нравится изобретать совершенно новый процесс; действительно, они предпочитают adopt существующий, который позволяет им избежать траты времени и денег на создание чего-то нового с нуля. Поскольку нет процесса, который подходит всем, вам нужно настроить ваш RUP для System z. В этой главе мы обсуждаем цель и цель настройки, объясняя, как создать план проекта, специфичный для вашего проекта, и как настроить RUP для System z с помощью Rational Method Composer.

#### 11.1 Введение

Фреймворк Rational Unified Process предоставляет рекомендации по богатому набору принципов программной инженерии. Он применим к проектам разных размеров и сложности, но это означает, что ни один отдельный проект не получит выгоды от использования всего RUP. Эта концепция также применима к уже адаптированному процессу (например, вы можете подумать о том, как ввести дальнейшую настройку в RUP для малых проектов), который может быть настроен для удовлетворения некоторых конкретных потребностей проекта. Эта концепция также верна для RUP для System z, то есть вы можете начать планировать свой проект, начиная с видов деятельности и задач, уже определенных в процессе поставки, но вы также можете понять, что некоторые конкретные потребности проекта могут подтолкнуть вас к добавлению, изменению и настройке определенных элементов процесса.

#### 11.2 Как создать план проекта, специфичный для вашего проекта

В этом разделе рассматривается создание плана проекта, специфичного для вашего проекта, путем идентификации фазовых итераций, видов деятельности и задач для выполнения и последующего создания плана проекта соответственно.

##### 11.2.1 Идентификация фазовых итераций, видов деятельности и задач для выполнения

Чтобы полностью понять, что вам нужно включить в ваш план проекта (или план итерации), мы рекомендуем сосредоточиться на том, какие фазовые итерации, виды деятельности и задачи выполнять. Более конкретно, чтобы создать план разработки, который позволяет вашей команде производить соответствующие рабочие продукты для вашего проекта, вам необходимо идентифицировать следующее:

- Сколько итераций на фазу необходимо для вашего проекта?
- Какие виды деятельности необходимо выполнять на каждой итерации?
- Какие задачи необходимо выполнять в каждом виде деятельности?

##### 11.2.2 Создание плана проекта

Теперь мы можем предположить, что у вас есть Development Case или хорошо определенный процесс для вашего проекта. Пришло время создать ваш план проекта (или итерации). Это можно сделать, экспортировав процесс поставки RUP для System z из RMC, затем импортировав его в инструмент управления проектами, такой как IBM Rational Portfolio Manager или Microsoft Project, и, наконец, изменив его, чтобы отразить ваш собственный специфический процесс, как определено в предыдущем разделе.

#### 11.3 Как настроить RUP для System z с помощью RMC

В этом разделе представлен подход к разработке методов с помощью IBM Rational Method Composer (RMC), который вы можете использовать для настройки RUP для System z для конкретной проектной команды или организации.

##### 11.3.1 Рабочие продукты разработки методов

Метод в первую очередь определяется в терминах элементов метода. Элемент метода может быть элементом содержания (роль, задача, рабочий продукт или руководство по содержанию) или элементом процесса (вид деятельности, шаблон возможностей, процесс поставки или руководство по процессу).

Основные рабочие продукты, специфичные для разработки методов, включают:

- **Эскиз метода:** Набросок метода, идентифицирующий кандидатов в элементы метода и, возможно, включающий некоторые их отношения и раннее описание.
- **Определение метода:** Хорошо сформированное определение метода с точки зрения его элементов метода (включая их описания), их отношений и характеристики одной или нескольких конфигураций метода.
- **Модуль метода:** Хорошо сформированное определение компонента метода (или всего метода, если метод определен с использованием только одного компонента) с точки зрения его элементов метода (включая их описание) и их отношений.
- **Конфигурация метода:** Характеристика версии метода.
- **Веб-сайт метода:** Основной результат проекта разработки методов. Он делает метод или методологический фреймворк доступным через набор взаимосвязанных веб-страниц.
- **Описание элемента метода:** Описание (то есть текстовое и графическое содержание) элемента содержания.

##### 11.3.2 Задачи разработки методов

Рабочие продукты, специфичные для разработки методов и представленные в предыдущем разделе, производятся путем выполнения задач, показанных на рисунке 11-7. Выполнение задач на рисунке 11-3 должно руководствоваться четким видением проекта и планом проекта (каким бы ни был их уровень формальности).

**Таблица 11-3. Описание задачи "Набросать метод"**

**Задача: Набросать метод**
Эта задача набрасывает метод в рамках эскиза метода. Она идентифицирует кандидатов в элементы метода и некоторые их отношения и предлагает раннее описание для некоторых ключевых элементов.

Некоторые показательные шаги для выполнения этой задачи предлагаются ниже (без определенного порядка):
- Определить стратегию разработки метода, такую как "сверху вниз" или "снизу вверх".
- Просмотреть существующие активы, такие как RUP для System z, и определить возможности повторного использования.
- Определить кандидатов в элементы метода (содержание и процессы), которые относятся к новому методу. Если применимо, различать элементы, которые находятся в объеме проекта, от элементов вне объема проекта (потому что они уже присутствуют в существующих методах и могут быть повторно использованы как есть, например).
- Определить кандидатные отношения между кандидатами в элементы метода (например, какая роль отвечает за рабочий продукт).
- Создать раннее описание для некоторых ключевых кандидатов в элементы метода.
- Получить обратную связь по эскизу метода от заинтересованных сторон.

**Таблица 11-4. Описание задачи "Структурировать метод"**

**Задача: Структурировать метод**
Эта задача структурирует метод с точки зрения модулей метода, пакетов метода, элементов метода, конфигураций метода и отношений между ними.

Некоторые показательные шаги для выполнения этой задачи предлагаются ниже (без определенного порядка):
- Если применимо, просмотреть структуру существующих модулей метода, образующих основу нового метода, таких как модули rup и rup_for_z.
- Определить модули метода, относящиеся к новому методу, и их зависимости от других модулей, если применимо.
- Определить пакеты метода в соответствующих модулях.
- Определить элементы метода в соответствующих пакетах и их отношения, включая отношения изменчивости для использования существующих активов.
- Логически категоризировать элементы метода, используя стандартные или пользовательские категории RMC.
- Определить представления навигации, используя пользовательские категории RMC.
- Определить конфигурации метода, выбирая набор модулей метода и пакетов метода для публикации, а также представления навигации для публикации.
- Получить обратную связь по структуре метода от заинтересованных сторон.

### 12. Выводы

Когда мы впервые начали проект Rational Unified Process (RUP) для System z, у нас было несколько основных вопросов:

- Действительно ли RUP применим к среде System z?
- Есть ли какие-либо части RUP, которые не применимы к среде System z?
- Как итерационная разработка реализуется в среде System z?
- Есть ли реальные преимущества для практиков System z?

Мы были полны решимости найти ответы на эти вопросы. Результат нашего поиска ответов был задокументирован в этой книге.

**Основные выводы:**
- Разрабатывая итеративно, мы смогли быстро построить и продемонстрировать базовую линию архитектуры приложения. Поскольку базовая линия архитектуры строилась с учетом наиболее рискованных и высокоприоритетных частей проекта, мы смогли продемонстрировать очень рано нашим заинтересованным сторонам и самим себе стабильную основу framework приложения. Мы продемонстрировали среду, которую мы можем легко улучшать и расширять в последующих итерациях. Эта стабильная основа гарантирует, что мы строим правильную систему.
- Более того, с каждой последующей итерацией мы постоянно обеспечивали и проверяли фактическим тестированием и реализацией частей приложения, которые мы построили к этому моменту, что приложение соответствовало существующим или измененным потребностям пользователей.
- Начав проверять рабочие продукты и тестировать компоненты приложения прямо с самых ранних итераций, мы смогли выявлять и исправлять дефекты раньше, а не позже. Как мы все знаем, выявление и исправление дефектов на раннем этапе обходится гораздо дешевле, чем исправление дефектов позже в жизненном цикле. В итоге мы построили более надежное и стабильное приложение по мере прогрессирования итераций.
- Обзоры проекта в конце итерации помогли показать команде разработчиков и нашим спонсорам проекта именно то, что мы достигли и что осталось достичь для каждой итерации и фазы. Деятельность по планированию проекта в RUP помогает определить четкие цели и критерии оценки для каждой итерации в рамках фазы, чтобы оценка того, что было достигнуто и что осталось сделать, была легким процессом. Планы проекта постоянно пересматривались и уточнялись на основе оценки рисков и приоритетов.

Исследуя RUP, мы обнаружили, что он, безусловно, очень применим к разработке приложений в среде System z. Мы надеемся, что эта книга и связанные с ней элементы, например, модуль метода RMC и примеры рабочих продуктов, помогут вам использовать RUP для System z с наилучшей выгодой для вашей организации.