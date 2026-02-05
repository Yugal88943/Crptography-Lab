\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{hcmut-report}

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax
\LoadClass[a4paper]{article}

\RequirePackage[utf8]{vntex,inputenc}
\RequirePackage{anyfontsize,amsmath,amssymb}
\RequirePackage[T5]{fontenc}

\RequirePackage{geometry,graphicx,indentfirst,setspace}
\RequirePackage{booktabs}
\RequirePackage[center]{caption}

\RequirePackage{fancyhdr,hyperref}
\RequirePackage[square,sort]{natbib}
\RequirePackage[nameinlink]{cleveref} % use \Cref{} instead of \ref{}

% Change to '[english,vietnamese]' to use Vietnamese labels
\RequirePackage[english]{babel}

% Draft watermark
% https://github.com/callegar/LaTeX-draftwatermark

% Custom commands
\newcommand{\Month}{
  \ifcase \the\month
  \or January
  \or February
  \or March
  \or April
  \or May
  \or June
  \or July
  \or August
  \or September
  \or October
  \or November
  \or December
  \fi
}

\newcommand{\@upperuniname}{Dr. B R Ambedkar National Institute of Technology, Jalandhar}

\newcommand{\@deptname}{Department of Computer Science & Engineering}
\newcommand{\deptname}[1]{\renewcommand{\@deptname}{#1}}

\newcommand{\@coursename}{Course name}
\newcommand{\coursename}[1]{\renewcommand{\@coursename}{#1}}

\newcommand{\@reporttype}{Assignment Report}
\newcommand{\reporttype}[1]{\renewcommand{\@reporttype}{#1}}

\renewcommand{\@title}{Report title}

\newcommand{\@presenter}{Presenter}
\newcommand{\presenter}[1]{\renewcommand{\@presenter}{#1}}

\newcommand{\@advisorOne}{Advisor One}
\newcommand{\advisorOne}[1]{\renewcommand{\@advisorOne}{#1}}

\newcommand{\@advisorTwo}{Advisor Two}
\newcommand{\advisorTwo}[1]{\renewcommand{\@advisorTwo}{#1}}

\newcommand{\@reportplace}{Jalandhar Punjab}
\newcommand{\reportplace}[1]{\renewcommand{\@reportplace}{#1}}

\newcommand{\@reporttime}{ \Month \the\year}
\newcommand{\reporttime}[1]{\renewcommand{\@reporttime}{#1}}

% Configurations
\geometry{
  paper=a4paper,
  left=3cm,
  right=2cm,
  vmargin=2cm,
  includeheadfoot=true,
  headheight=30pt
}

\onehalfspacing
\raggedbottom

\AtBeginDocument{\renewcommand*\bibname{References}}

\hypersetup{
  colorlinks=true,
  linkcolor=black,
  citecolor=red,
  urlcolor=blue
}

\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

\pagestyle{fancy}
\fancyhf{}

\fancyfoot[C]{\thepage}

% Custom pages and sections
\newcommand{\coverpage}{
  \pagestyle{empty}

  \vspace*{-3\baselineskip}
  \begin{center}
    \MakeUppercase{\Large\@upperuniname}

    \MakeUppercase{\@uniname}

    \MakeUppercase{\@deptname}
    \vfill
    \includegraphics[scale=0.4]{graphics/logo.jpg}
    \vfill
    \bfseries
    \begin{tabular}{c}
      \Large\@coursename                                 \\
      {}                                                 \\
      \midrule                                           \\
      {}                                                 \\
      \Large\@reporttype                                 \\
      {}                                                 \\
      \LARGE\parbox[c]{0.85\linewidth}{\centering \@title} \\
      {}                                                 \\
      \bottomrule
    \end{tabular}
    \vfill
    \mdseries
    \begin{tabular}{rll}
      Presented by: & \@presenter & \\
      %Student: & Name      & ID \\
    \end{tabular}
      \vfill

\begin{tabular}{rl}
     Supervisor: & \\ \@advisorOne \\
      
\end{tabular}
\hfill
\begin{tabular}{rl}
      Supervisor: & \\ \@advisorTwo \\
      
\end{tabular}

    \vfill
    \MakeUppercase{\@reportplace, \@reporttime}
  \end{center}

  \cleardoublepage
  \pagestyle{fancy}
}
