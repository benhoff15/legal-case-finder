export interface Case {
  id: number;
  title: string;
  case_summary?: string;
  full_text?: string;
  charges?: string;
  defendant_age?: number;
  defendant_race?: string;
  state?: string;
  year?: number;
  court_type?: string;
  keywords?: string;
}
